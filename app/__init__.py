 from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'
    migrate.init_app(app, db)



    # Make config available in templates
    @app.context_processor
    def inject_config():
        return dict(config=app.config)

    # Blueprints
    from app.views import main_bp
    from app.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/admin')

    # Initialize database tables
    with app.app_context():
        try:
            db.create_all()
            
            # Create admin user if it doesn't exist
            from app.models import User, Project
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                admin = User(username='admin', email='admin@portfolio.com')
                admin.set_password('admin123')
                db.session.add(admin)
                
                # Create guest user
                guest = User(username='guest', email='guest@portfolio.demo')
                guest.set_password('guest123')
                db.session.add(guest)
                
                # Create sample project
                sample_project = Project(
                    title='Portfolio CMS Demo',
                    description='A modern portfolio management system built with Flask. Features include user authentication, project management, and responsive design.',
                    url='https://github.com/sanjujohn8055/portfolio-for-content-management-sytem',
                    user_id=None  # Demo project
                )
                db.session.add(sample_project)
                
                db.session.commit()
        except Exception as e:
            print(f"Database initialization error: {e}")
            # Continue anyway - database might already exist

    return app
