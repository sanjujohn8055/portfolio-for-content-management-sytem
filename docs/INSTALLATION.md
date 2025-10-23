# Portfolio CMS - Installation & Setup Guide

## Prerequisites

- **Python 3.8+** installed on your system
- **Git** for version control
- **Web browser** (Chrome, Firefox, Safari, Edge)
- **Internet connection** for dependency installation

## Quick Start (5 minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/portfolio-cms.git
cd portfolio-cms
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database & Demo Data
```bash
python setup_demo.py
```

### 5. Run the Application
```bash
python run.py
```

### 6. Access the Application
Open your web browser and navigate to:
- **Main Site**: http://localhost:5000
- **Admin Login**: http://localhost:5000/admin/login

## Default Login Credentials

### Admin Account
- **Username**: `admin`
- **Password**: `admin123`

### Guest Mode
- Click "Try Demo Mode" on any login/signup page
- No credentials required

## Detailed Installation

### Environment Setup

1. **Check Python Version**
   ```bash
   python --version
   # Should be 3.8 or higher
   ```

2. **Create Project Directory**
   ```bash
   mkdir portfolio-cms
   cd portfolio-cms
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/portfolio-cms.git .
   ```

### Virtual Environment Configuration

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   
   **Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate
   ```
   
   **Windows (PowerShell):**
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

3. **Verify Activation**
   ```bash
   which python  # Should point to venv/bin/python
   ```

### Dependency Installation

1. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**
   ```bash
   pip list
   # Should show Flask, SQLAlchemy, etc.
   ```

### Database Setup

1. **Initialize Database**
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database created!')"
   ```

2. **Load Demo Data**
   ```bash
   python setup_demo.py
   ```

### Configuration

1. **Environment Variables** (Optional)
   Create `.env` file:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

2. **Database Configuration** (Optional)
   For production, update `app/config.py`:
   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@localhost/dbname'
   ```

## Running the Application

### Development Mode
```bash
python run.py
```
- Runs on http://localhost:5000
- Debug mode enabled
- Auto-reload on code changes

### Production Mode
```bash
gunicorn --bind 0.0.0.0:5000 run:app
```

## Docker Deployment

### Using Docker Compose

1. **Create docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     web:
       build: .
       ports:
         - "5000:5000"
       environment:
         - SECRET_KEY=production-secret-key
         - DATABASE_URL=sqlite:///data.sqlite
       volumes:
         - ./:/app
   ```

2. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

## Cloud Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Create Heroku App**
   ```bash
   heroku create your-portfolio-cms
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=your-production-secret
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### AWS/DigitalOcean Deployment

1. **Set up server** (Ubuntu 20.04 recommended)
2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip nginx
   ```

3. **Clone and setup application**
4. **Configure Nginx** as reverse proxy
5. **Set up SSL certificate** (Let's Encrypt)

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Kill process on port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Permission Denied (Windows)**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Database Locked**
   ```bash
   # Remove database file and recreate
   rm data.sqlite
   python setup_demo.py
   ```

4. **Module Not Found**
   ```bash
   # Ensure virtual environment is activated
   pip install -r requirements.txt
   ```

### Performance Issues

1. **Slow Loading**
   - Check database size
   - Optimize queries
   - Enable caching

2. **Memory Usage**
   - Monitor with `htop` or Task Manager
   - Consider upgrading server resources

### Security Checklist

- [ ] Change default admin password
- [ ] Set strong SECRET_KEY in production
- [ ] Enable HTTPS in production
- [ ] Regular security updates
- [ ] Monitor access logs

## Development Setup

### Code Structure
```
portfolio-cms/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── views.py             # Main routes
│   ├── auth.py              # Authentication routes
│   ├── forms.py             # WTForms definitions
│   ├── config.py            # Configuration
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
├── docs/                    # Documentation
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
├── setup_demo.py           # Demo data setup
└── README.md               # Project overview
```

### Development Workflow

1. **Make Changes**
2. **Test Locally**
   ```bash
   python run.py
   ```
3. **Run Tests**
   ```bash
   pytest tests/
   ```
4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

## Support

### Getting Help
- Check documentation in `docs/` folder
- Review error logs in terminal
- Search GitHub issues
- Contact project maintainer

### Reporting Issues
1. Check existing issues on GitHub
2. Provide detailed error messages
3. Include system information
4. Steps to reproduce the problem

## Next Steps

After successful installation:
1. **Explore the demo** - Try guest mode
2. **Create your account** - Sign up with your details
3. **Add your projects** - Showcase your work
4. **Customize appearance** - Modify CSS if needed
5. **Deploy to production** - Share your portfolio with the world