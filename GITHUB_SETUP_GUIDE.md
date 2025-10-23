# 🚀 GitHub Setup & Deployment Guide

## Step 1: Install Git (if needed)

### Windows
1. Download Git from: https://git-scm.com/download/win
2. Run installer with default settings
3. Restart your terminal/PowerShell

### Verify Installation
```bash
git --version
# Should show: git version 2.x.x
```

## Step 2: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Sign in** or create account
3. **Click "New Repository"** (green button)
4. **Repository Settings**:
   - Name: `portfolio-cms`
   - Description: `Professional Portfolio Management System - Flask Web Application`
   - Visibility: **Public** ✅
   - **Don't** initialize with README (we have one)
5. **Click "Create Repository"**

## Step 3: Push Your Project

### In your project directory, run:

```bash
# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Complete Portfolio CMS with documentation and tests"

# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/portfolio-cms.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Cloud (Choose One)

### Option A: Heroku (Recommended - Free Tier)

1. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
2. **Login to Heroku**:
   ```bash
   heroku login
   ```
3. **Create Heroku App**:
   ```bash
   heroku create your-portfolio-cms
   ```
4. **Deploy**:
   ```bash
   git push heroku main
   ```
5. **Your live URL**: `https://your-portfolio-cms.herokuapp.com`

### Option B: Railway (Easy Alternative)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `portfolio-cms` repository
5. Railway auto-deploys your app
6. Get your live URL from Railway dashboard

### Option C: Render (Another Free Option)

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New Web Service"
4. Connect your `portfolio-cms` repository
5. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
6. Deploy and get your live URL

## Step 5: Verify Deployment

### Test Your Live Application
1. **Visit your live URL**
2. **Test key features**:
   - Landing page loads
   - "Try Demo Mode" works
   - User registration works
   - Project creation works
   - Portfolio URLs work (`/portfolio/admin`)

### Update README with Live URLs
```markdown
## 🚀 Live Demo
- **Live Application**: https://your-app-url.com
- **Demo Portfolio**: https://your-app-url.com/demo
- **Admin Panel**: https://your-app-url.com/admin/login
```

## Step 6: Final Submission Package

### Create submission.txt file:
```txt
Portfolio CMS - Professional Portfolio Management System

GitHub Repository: https://github.com/YOUR_USERNAME/portfolio-cms
Live Application: https://your-app-url.com
Demo Portfolio: https://your-app-url.com/demo

Login Credentials:
- Username: admin
- Password: admin123
- Guest Mode: Click "Try Demo Mode" (no login required)

Key Features:
- User registration and authentication
- Project management (CRUD operations)
- Individual portfolio URLs
- Responsive design
- Admin dashboard
- Guest mode for demos

Technologies Used:
- Backend: Flask, SQLAlchemy, Python
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
- Database: SQLite (dev), PostgreSQL (production)
- Deployment: Docker, Heroku/Railway/Render
```

## Troubleshooting

### Common Git Issues

**"Git not recognized"**
```bash
# Restart terminal after installing Git
# Or add Git to PATH manually
```

**"Permission denied"**
```bash
# Use HTTPS instead of SSH for first time
git remote set-url origin https://github.com/YOUR_USERNAME/portfolio-cms.git
```

**"Repository not found"**
```bash
# Make sure repository name matches exactly
# Check if repository is public
```

### Deployment Issues

**Heroku Build Failed**
```bash
# Check requirements.txt is complete
# Ensure Procfile exists (optional for Python)
# Check Heroku logs: heroku logs --tail
```

**App Won't Start**
```bash
# Check environment variables
# Verify gunicorn is in requirements.txt
# Check application logs
```

## Success Checklist

- [ ] Git installed and working
- [ ] GitHub repository created (public)
- [ ] Code pushed to GitHub successfully
- [ ] Application deployed to cloud platform
- [ ] Live URL accessible and working
- [ ] All key features tested on live site
- [ ] Demo credentials working
- [ ] README updated with live URLs
- [ ] submission.txt file created

## 🎉 You're Done!

Your Portfolio CMS is now:
✅ **Version controlled** on GitHub  
✅ **Live on the internet** via cloud deployment  
✅ **Fully documented** with comprehensive guides  
✅ **Ready for submission** with all requirements met  

**Congratulations on building a professional-grade web application!** 🚀