# Blog

A platform where users can register, log in, and share their thoughts via tweets. Users can create, edit, delete, and comment on tweets categorized under tags like "Personal," "Business," "Food," "Product," and "Travel." Built with Django.

## Features

- **User Authentication**: Register, log in, and log out.  
- **Tweet Management**: Create, edit, and delete tweets.  
- **Comments**: Add comments on tweets.  
- **Tagging**: Categorize tweets with tags.  
- **Dashboard**: View and manage tweets.  
- **Recent Tweets**: Display the latest tweets.

## Technologies Used

- **Django** for backend.
- **HTML/CSS**: Structure and design
- **Bootstrap** for styling.
- **SQLite** for database.  

---

### Setup Instructions

```bash
# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Apply migrations and start the server
python manage.py migrate
python manage.py runserver

# Open the app at
http://127.0.0.1:8000/
