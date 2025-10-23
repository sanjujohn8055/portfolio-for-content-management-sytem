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

    with app.app_context():
        db.create_all()  # simple approach for SQLite early dev

    return app
