import pytest
from app import create_app, db
from app.models import Project, User

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    with app.app_context():
        db.create_all()
        yield app

def test_add_project(app):
    with app.app_context():
        p = Project(title="Test", description="Desc")
        db.session.add(p)
        db.session.commit()
        assert Project.query.count() == 1
