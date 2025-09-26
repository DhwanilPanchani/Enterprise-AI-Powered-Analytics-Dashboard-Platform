# Analytics Platform

A modern analytics platform with AI-powered data analysis capabilities.

## Features

- **User Authentication**: Secure login/registration system
- **Real-time Analytics**: Interactive charts and data visualization
- **AI Data Analyst**: Natural language queries about your data
- **Modern UI**: Beautiful, responsive interface with smooth animations
- **Docker Support**: Easy deployment with Docker Compose

## Tech Stack

- **Backend**: Django REST Framework
- **Frontend**: React with Tailwind CSS
- **Database**: PostgreSQL + MongoDB
- **AI**: Custom rule-based analysis (no external API required)
- **Deployment**: Docker & Docker Compose

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd analytics-platform
   ```

2. **Set up environment variables**
   ```bash
   # Create .env file in the root directory
   cp .env.example .env
   
   # Edit .env with your actual values:
   DJANGO_SECRET_KEY=your-django-secret-key-here
   OPENAI_API_KEY=your-openai-api-key-here  # Optional
   ```

3. **Start the application**
   ```bash
   docker compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000 (or serve index.html)
   - Backend API: http://localhost:8000
   - Ingestion Service: http://localhost:5001

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Django Secret Key (required)
DJANGO_SECRET_KEY=your-django-secret-key-here

# OpenAI API Key (optional - for AI features)
OPENAI_API_KEY=your-openai-api-key-here

# Database Configuration (optional - defaults provided)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=db-users
```

## API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login

### Data Management
- `GET /api/data` - Get analytics data (requires authentication)
- `POST /api/ingest` - Ingest new data
- `POST /api/nlq` - Natural language queries (requires authentication)

## Project Structure

```
analytics-platform/
├── backend/                 # Django REST API
│   ├── user_service/       # Django project settings
│   ├── users/              # User management app
│   └── requirements.txt    # Python dependencies
├── ingestion_service/      # Flask data ingestion service
│   ├── app.py             # Main Flask application
│   └── requirements.txt   # Python dependencies
├── frontend/               # React frontend
│   └── index.html         # Single-page application
├── docker-compose.yml      # Docker services configuration
└── .env                    # Environment variables (create this)
```

## Development

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

### Frontend Development
The frontend is a single HTML file with embedded React. No build process required.

## Security Notes

- Never commit `.env` files to version control
- Use strong, unique secret keys in production
- Configure proper CORS settings for production
- Use HTTPS in production environments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
