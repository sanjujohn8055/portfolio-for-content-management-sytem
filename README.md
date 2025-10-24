# Portfolio CMS - Professional Portfolio Management System

A modern, responsive web application that enables developers and professionals to create, manage, and share beautiful portfolios with ease.

## 🚀 Live Demo

- **Live Application**: [Portfolio CMS](https://web-production-846c5.up.railway.app)
- **Demo Portfolio**: [View Demo](https://web-production-846c5.up.railway.app/demo)
- **Admin Panel**: [Try Guest Mode](https://web-production-846c5.up.railway.app/admin/login)

### Login Credentials
- **Admin**: username `admin`, password `admin123`
- **Guest Mode**: Click "Try Demo Mode" (no login required)

## ✨ Features

### 🎯 **Core Functionality**
- **User Registration & Authentication** - Secure account creation and login
- **Project Management** - Full CRUD operations for portfolio projects
- **Individual Portfolio URLs** - Each user gets a shareable portfolio link
- **Admin Dashboard** - Intuitive interface for content management
- **Guest Mode** - Try all features without creating an account

### 🎨 **Design & UX**
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Modern UI** - Clean, professional interface with smooth animations
- **Intuitive Navigation** - Self-explanatory user interface
- **Professional Templates** - Beautiful portfolio layouts

### 🔧 **Technical Features**
- **Secure Authentication** - Password hashing and session management
- **Data Validation** - Comprehensive form validation and error handling
- **Performance Optimized** - Fast loading times and efficient queries
- **SEO Friendly** - Proper meta tags and semantic HTML

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.4** - Python web framework
- **SQLAlchemy 3.0.3** - Database ORM
- **Flask-Login 0.6.2** - User session management
- **Flask-WTF 1.1.1** - Form handling and CSRF protection

### Frontend
- **HTML5 & CSS3** - Modern web standards
- **Bootstrap 5.3** - Responsive framework
- **JavaScript** - Interactive functionality
- **Bootstrap Icons** - Consistent iconography

### Database
- **SQLite** - Development database
- **PostgreSQL** - Production ready (configurable)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio-cms.git
   cd portfolio-cms
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database and demo data**
   ```bash
   python setup_demo.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Open in browser**
   - Main site: http://localhost:5000
   - Admin login: http://localhost:5000/admin/login

### Default Credentials
- **Username**: `admin`
- **Password**: `admin123`

## 📖 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[Project Profile](docs/PROJECT_PROFILE.md)** - Project overview and objectives
- **[Requirements](docs/REQUIREMENTS.md)** - Functional and non-functional requirements
- **[Architecture](docs/ARCHITECTURE.md)** - System design and technical documentation

## 🎯 Use Cases

### For Developers
- Showcase coding projects and technical skills
- Share portfolio with potential employers
- Demonstrate project progression and growth

### For Designers
- Display creative work and design projects
- Create professional online presence
- Share portfolio with clients and agencies

### For Students
- Document academic projects and achievements
- Build professional portfolio for job applications
- Demonstrate learning progress and skills

## 🌟 Key Benefits

### **Easy to Use**
- Intuitive admin interface
- No technical knowledge required
- Quick project addition and editing

### **Professional Results**
- Modern, responsive design
- SEO-optimized portfolio pages
- Professional URLs for sharing

### **Secure & Reliable**
- Secure user authentication
- Data protection and privacy
- Reliable hosting and performance

## 📱 Screenshots

### Landing Page
Beautiful marketing page that showcases the platform's value proposition.

### Admin Dashboard
Clean, intuitive interface for managing projects and portfolio content.

### Portfolio View
Professional portfolio display with responsive design and modern aesthetics.

## 🔧 Development

### Project Structure
```
portfolio-cms/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── views.py             # Main application routes
│   ├── auth.py              # Authentication routes
│   ├── forms.py             # WTForms definitions
│   ├── config.py            # Configuration settings
│   ├── static/              # CSS, JS, images
│   └── templates/           # Jinja2 HTML templates
├── docs/                    # Project documentation
├── tests/                   # Unit and integration tests
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── setup_demo.py           # Demo data initialization
```

### Running Tests
```bash
pytest tests/
```

### Code Quality
- Clean, documented code
- Separation of concerns
- Security best practices
- Performance optimization

## 🚀 Deployment

### Docker
```bash
docker-compose up --build
```

### Cloud Platforms
- **Heroku**: Ready for deployment
- **AWS**: EC2 or Elastic Beanstalk
- **DigitalOcean**: App Platform or Droplets
- **Google Cloud**: App Engine or Compute Engine

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Bootstrap team for responsive framework
- Contributors and testers who provided feedback

## 📞 Support

- **Documentation**: Check the `docs/` folder
- **Issues**: Report bugs on GitHub Issues
- **Questions**: Contact the maintainer

---

**Built with ❤️ for the developer community**