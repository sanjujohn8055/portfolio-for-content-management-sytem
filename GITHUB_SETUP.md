# GitHub OAuth Setup Guide

To enable GitHub login and automatic repository import, follow these steps:

## 1. Create a GitHub OAuth App

1. Go to [GitHub Settings](https://github.com/settings/developers)
2. Click "OAuth Apps" in the left sidebar
3. Click "New OAuth App"
4. Fill in the details:
   - **Application name**: Portfolio CMS
   - **Homepage URL**: http://localhost:5000
   - **Authorization callback URL**: http://localhost:5000/auth/github/authorized
5. Click "Register application"

## 2. Get Your Credentials

After creating the app, you'll see:
- **Client ID**: Copy this value
- **Client Secret**: Click "Generate a new client secret" and copy it

## 3. Update Your Environment

Edit your `.env` file and replace the placeholder values:

```env
GITHUB_CLIENT_ID=your-actual-client-id-here
GITHUB_CLIENT_SECRET=your-actual-client-secret-here
```

## 4. Restart the Application

```bash
# Stop the current server (Ctrl+C)
# Then restart:
python run.py
```

## 5. Test GitHub Login

1. Visit http://localhost:5000
2. Click "Sign Up" or "Login"
3. Click "Continue with GitHub"
4. Authorize the application
5. Your repositories will be automatically imported as projects!

## Features

- **Automatic Account Creation**: New users are created from GitHub profile
- **Repository Import**: Your public repositories become portfolio projects
- **Profile Integration**: GitHub avatar and username are used
- **Seamless Login**: One-click authentication

## Note

Without GitHub OAuth setup, you can still:
- Create accounts manually using the signup form
- Login with username/password
- Add projects manually through the admin panel

The existing admin account (username: `admin`, password: `admin123`) will continue to work.