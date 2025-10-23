#!/usr/bin/env python3
"""
Demo setup script for the Portfolio CMS
Creates a default admin user and sample projects
"""

from app import create_app, db
from app.models import User, Project

def setup_demo_data():
    app = create_app()
    
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if admin user already exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            # Create admin user
            admin = User(username='admin')
            admin.set_password('admin123')  # Change this in production!
            db.session.add(admin)
            print("✓ Created admin user (username: admin, password: admin123)")
        else:
            print("✓ Admin user already exists")
        
        # Create guest user for demo purposes
        guest_user = User.query.filter_by(username='guest').first()
        if not guest_user:
            guest_user = User(
                username='guest',
                email='guest@portfolio.demo'
            )
            guest_user.set_password('guest123')
            db.session.add(guest_user)
            print("✓ Created guest user for demo mode")
        
        # Check if sample projects exist
        if Project.query.count() == 0:
            # Create sample projects
            projects = [
                {
                    'title': 'E-Commerce Website',
                    'description': '''A full-featured e-commerce platform built with Flask and SQLAlchemy. 
                    
Features include:
• User authentication and authorization
• Product catalog with search and filtering
• Shopping cart and checkout system
• Admin dashboard for inventory management
• Responsive design with Bootstrap
• Payment integration with Stripe
• Email notifications for orders

Technologies used: Python, Flask, SQLAlchemy, Bootstrap, JavaScript, Stripe API''',
                    'url': 'https://github.com/yourusername/ecommerce-flask',
                    'image': None
                },
                {
                    'title': 'Task Management App',
                    'description': '''A collaborative task management application similar to Trello, built with modern web technologies.

Key features:
• Drag-and-drop task boards
• Real-time collaboration
• User roles and permissions
• File attachments and comments
• Due date reminders
• Progress tracking and analytics
• Mobile-responsive interface

Built with Flask, Socket.IO for real-time features, and PostgreSQL for data persistence.''',
                    'url': 'https://github.com/yourusername/task-manager',
                    'image': None
                },
                {
                    'title': 'Weather Dashboard',
                    'description': '''An interactive weather dashboard that provides current conditions and forecasts for multiple cities.

Features:
• Current weather conditions
• 7-day weather forecast
• Interactive maps with weather overlays
• Location-based weather detection
• Weather alerts and notifications
• Historical weather data charts
• Favorite locations management

Integrates with OpenWeatherMap API and uses Chart.js for data visualization.''',
                    'url': 'https://weather-dashboard-demo.herokuapp.com',
                    'image': None
                },
                {
                    'title': 'Blog Platform',
                    'description': '''A modern blogging platform with content management capabilities and SEO optimization.

Core functionality:
• Rich text editor for content creation
• Category and tag management
• Comment system with moderation
• SEO-friendly URLs and meta tags
• Social media integration
• RSS feed generation
• Analytics dashboard
• Multi-author support

Built with Flask, CKEditor for rich text editing, and optimized for search engines.''',
                    'url': None,
                    'image': None
                }
            ]
            
            for project_data in projects:
                project_data['user_id'] = None  # Demo projects have no owner
                project = Project(**project_data)
                db.session.add(project)
            
            print(f"✓ Created {len(projects)} sample projects")
        else:
            print(f"✓ Found {Project.query.count()} existing projects")
        
        # Commit all changes
        db.session.commit()
        print("\n🎉 Demo setup complete!")
        print("\nYou can now:")
        print("1. Run the app: python run.py")
        print("2. Visit: http://localhost:5000")
        print("3. Admin login: http://localhost:5000/admin/login")
        print("   Username: admin")
        print("   Password: admin123")

if __name__ == '__main__':
    setup_demo_data()