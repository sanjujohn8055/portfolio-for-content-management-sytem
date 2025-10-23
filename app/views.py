from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Project, User
from .forms import ProjectForm
from . import db
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Show a landing page for the portfolio platform
    return render_template('landing.html')

@main_bp.route('/portfolio/<username>')
def user_portfolio(username):
    # Show a specific user's portfolio
    user = User.query.filter_by(username=username).first_or_404()
    projects = Project.query.filter_by(user_id=user.id).order_by(Project.created_at.desc()).all()
    return render_template('portfolio.html', user=user, projects=projects)

@main_bp.route('/demo')
def demo_portfolio():
    # Show the demo portfolio with sample projects
    projects = Project.query.filter_by(user_id=None).order_by(Project.created_at.desc()).all()
    return render_template('portfolio.html', user=None, projects=projects, is_demo=True)

@main_bp.route('/projects')
def projects():
    # Redirect to user's portfolio or demo
    if current_user.is_authenticated:
        return redirect(url_for('main.user_portfolio', username=current_user.username))
    else:
        return redirect(url_for('main.demo_portfolio'))

@main_bp.route('/project/<int:project_id>')
def project_detail(project_id):
    p = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=p)

# Admin routes
@main_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.username == 'guest':
        # Guest sees demo projects
        projects = Project.query.filter_by(user_id=None).order_by(Project.created_at.desc()).all()
    else:
        # Users see their own projects
        projects = Project.query.filter_by(user_id=current_user.id).order_by(Project.created_at.desc()).all()
    return render_template('admin/dashboard.html', projects=projects)

@main_bp.route('/admin/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        user_id = None if current_user.username == 'guest' else current_user.id
        p = Project(
            title=form.title.data, 
            description=form.description.data, 
            url=form.url.data, 
            image=form.image.data,
            user_id=user_id
        )
        db.session.add(p)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('main.admin_dashboard'))
    return render_template('admin/new_project.html', form=form)

@main_bp.route('/admin/project/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    p = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=p)
    if form.validate_on_submit():
        p.title = form.title.data
        p.description = form.description.data
        p.url = form.url.data
        p.image = form.image.data
        db.session.commit()
        flash('Project updated', 'success')
        return redirect(url_for('main.admin_dashboard'))
    return render_template('admin/edit_project.html', form=form, project=p)

@main_bp.route('/admin/project/<int:project_id>/delete', methods=['POST'])
@login_required
def delete_project(project_id):
    p = Project.query.get_or_404(project_id)
    db.session.delete(p)
    db.session.commit()
    flash('Project deleted', 'success')
    return redirect(url_for('main.admin_dashboard'))
