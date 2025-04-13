# Memelib

A Django-based meme sharing application with download and like functionality.

## Features

- Meme upload and sharing
- Download counter
- Like/unlike system
- User authentication
- Modern UI with Bootstrap

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd memelib
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create necessary directories:
```bash
mkdir -p media/memes static staticfiles
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

8. Access the application at `http://localhost:8000`

## File Structure

```
memelib/
├── memes/              # Main app
├── memelib/            # Project settings
├── templates/          # HTML templates
├── static/            # Static files
├── media/             # Uploaded files
└── staticfiles/       # Collected static files
```

## Linux Compatibility

The project is designed to be compatible with Linux systems. Key points:
- Uses forward slashes in file paths
- Compatible with Linux file permissions
- Uses environment variables for configuration
- Follows Linux directory structure conventions 