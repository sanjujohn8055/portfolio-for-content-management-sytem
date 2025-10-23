import pytest
from app import create_app, db
from app.models import User, Project

@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SECRET_KEY": "test-secret-key",
        "WTF_CSRF_ENABLED": False
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create test runner."""
    return app.test_cli_runner()

@pytest.fixture
def test_user(app):
    """Create test user."""
    user = User(username='testuser', email='test@example.com')
    user.set_password('testpass123')
    db.session.add(user)
    db.session.commit()
    return user

class TestAuthentication:
    """Test user authentication functionality."""
    
    def test_user_registration(self, client):
        """Test user can register successfully."""
        response = client.post('/admin/signup', data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
            'submit': 'Sign Up'
        })
        assert response.status_code == 302  # Redirect after successful registration
        
        # Verify user was created
        user = User.query.filter_by(username='newuser').first()
        assert user is not None
        assert user.email == 'new@example.com'
    
    def test_user_login(self, client, test_user):
        """Test user can login successfully."""
        response = client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpass123',
            'submit': 'Login'
        })
        assert response.status_code == 302  # Redirect after successful login
    
    def test_invalid_login(self, client, test_user):
        """Test login fails with invalid credentials."""
        response = client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'wrongpassword',
            'submit': 'Login'
        })
        assert b'Invalid username or password' in response.data
    
    def test_guest_login(self, client):
        """Test guest mode access."""
        response = client.get('/admin/guest')
        assert response.status_code == 302  # Redirect to dashboard

class TestProjectManagement:
    """Test project CRUD operations."""
    
    def test_create_project(self, client, test_user):
        """Test project creation."""
        # Login first
        client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Create project
        response = client.post('/admin/project/new', data={
            'title': 'Test Project',
            'description': 'A test project description',
            'url': 'https://github.com/test/project',
            'image': 'test.jpg',
            'submit': 'Save'
        })
        assert response.status_code == 302
        
        # Verify project was created
        project = Project.query.filter_by(title='Test Project').first()
        assert project is not None
        assert project.user_id == test_user.id
    
    def test_view_project(self, client, test_user):
        """Test project detail view."""
        # Create a project
        project = Project(
            title='View Test Project',
            description='Test description',
            user_id=test_user.id
        )
        db.session.add(project)
        db.session.commit()
        
        response = client.get(f'/project/{project.id}')
        assert response.status_code == 200
        assert b'View Test Project' in response.data
    
    def test_edit_project(self, client, test_user):
        """Test project editing."""
        # Create a project
        project = Project(
            title='Original Title',
            description='Original description',
            user_id=test_user.id
        )
        db.session.add(project)
        db.session.commit()
        
        # Login
        client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Edit project
        response = client.post(f'/admin/project/{project.id}/edit', data={
            'title': 'Updated Title',
            'description': 'Updated description',
            'url': '',
            'image': '',
            'submit': 'Save'
        })
        assert response.status_code == 302
        
        # Verify changes
        updated_project = Project.query.get(project.id)
        assert updated_project.title == 'Updated Title'
    
    def test_delete_project(self, client, test_user):
        """Test project deletion."""
        # Create a project
        project = Project(
            title='Delete Me',
            description='To be deleted',
            user_id=test_user.id
        )
        db.session.add(project)
        db.session.commit()
        project_id = project.id
        
        # Login
        client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Delete project
        response = client.post(f'/admin/project/{project_id}/delete')
        assert response.status_code == 302
        
        # Verify deletion
        deleted_project = Project.query.get(project_id)
        assert deleted_project is None

class TestPortfolioViews:
    """Test portfolio display functionality."""
    
    def test_landing_page(self, client):
        """Test landing page loads correctly."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Build Your Professional Portfolio' in response.data
    
    def test_demo_portfolio(self, client):
        """Test demo portfolio page."""
        response = client.get('/demo')
        assert response.status_code == 200
        assert b'Demo Portfolio' in response.data
    
    def test_user_portfolio(self, client, test_user):
        """Test individual user portfolio."""
        response = client.get(f'/portfolio/{test_user.username}')
        assert response.status_code == 200
        assert test_user.username.encode() in response.data
    
    def test_nonexistent_portfolio(self, client):
        """Test 404 for nonexistent user portfolio."""
        response = client.get('/portfolio/nonexistentuser')
        assert response.status_code == 404

class TestSecurity:
    """Test security features."""
    
    def test_admin_requires_login(self, client):
        """Test admin pages require authentication."""
        response = client.get('/admin/dashboard')
        assert response.status_code == 302  # Redirect to login
    
    def test_project_isolation(self, client):
        """Test users can only see their own projects."""
        # Create two users
        user1 = User(username='user1', email='user1@test.com')
        user1.set_password('pass123')
        user2 = User(username='user2', email='user2@test.com')
        user2.set_password('pass123')
        
        db.session.add_all([user1, user2])
        db.session.commit()
        
        # Create projects for each user
        project1 = Project(title='User1 Project', description='Desc1', user_id=user1.id)
        project2 = Project(title='User2 Project', description='Desc2', user_id=user2.id)
        
        db.session.add_all([project1, project2])
        db.session.commit()
        
        # Login as user1
        client.post('/admin/login', data={
            'username': 'user1',
            'password': 'pass123'
        })
        
        # Check dashboard only shows user1's projects
        response = client.get('/admin/dashboard')
        assert b'User1 Project' in response.data
        assert b'User2 Project' not in response.data

class TestFormValidation:
    """Test form validation."""
    
    def test_registration_validation(self, client):
        """Test registration form validation."""
        # Test password mismatch
        response = client.post('/admin/signup', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'different',
            'submit': 'Sign Up'
        })
        assert b'Passwords must match' in response.data
    
    def test_project_validation(self, client, test_user):
        """Test project form validation."""
        # Login
        client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Test empty title
        response = client.post('/admin/project/new', data={
            'title': '',
            'description': 'Valid description',
            'submit': 'Save'
        })
        assert response.status_code == 200  # Form redisplayed with errors

class TestModels:
    """Test database models."""
    
    def test_user_password_hashing(self):
        """Test password hashing functionality."""
        user = User(username='testuser', email='test@example.com')
        user.set_password('mypassword')
        
        assert user.password_hash is not None
        assert user.password_hash != 'mypassword'
        assert user.check_password('mypassword') is True
        assert user.check_password('wrongpassword') is False
    
    def test_user_project_relationship(self, app):
        """Test User-Project relationship."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password')
            db.session.add(user)
            db.session.commit()
            
            project = Project(
                title='Test Project',
                description='Test description',
                user_id=user.id
            )
            db.session.add(project)
            db.session.commit()
            
            # Test relationship
            assert len(user.projects) == 1
            assert user.projects[0].title == 'Test Project'
            assert project.user.username == 'testuser'

if __name__ == '__main__':
    pytest.main([__file__])