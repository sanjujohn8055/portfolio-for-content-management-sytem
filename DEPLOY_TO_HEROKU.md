# 🚀 Deploy Portfolio CMS to Heroku

## Quick Deployment Steps

### 1. Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create Heroku App
```bash
heroku create portfolio-cms-sanju
```

### 4. Deploy
```bash
git push heroku main
```

### 5. Initialize Database
```bash
heroku run python setup_demo.py
```

### 6. Open Your App
```bash
heroku open
```

## Alternative: Railway (Easier)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository: `portfolio-for-content-management-sytem`
5. Railway will auto-deploy!

## Alternative: Render (Free)

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New Web Service"
4. Connect your repository
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
6. Deploy!

## Your App Will Be Live At:
- Heroku: `https://portfolio-cms-sanju.herokuapp.com`
- Railway: `https://your-app.railway.app`
- Render: `https://your-app.onrender.com`