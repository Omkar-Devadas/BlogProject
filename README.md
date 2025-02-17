
A platform where users can register, log in, and share their thoughts via tweets. Users can create, edit, delete, and comment on tweets categorized under tags like "Personal," "Business," "Food," "Product," and "Travel." Built with Django.

## Features

- **User Authentication**: Register, log in, and log out.  
- **Tweet Management**: Create, edit, and delete tweets.  
- **Comments**: Add comments on tweets.  
- **Tagging**: Categorize tweets with tags.  
- **Dashboard**: View and manage tweets.  
- **Recent Tweets**: Display the latest tweets.



**HOME PAGE**
![home](https://github.com/user-attachments/assets/36df7bd5-94df-47f3-8eea-c270bfc4d238)# Blog


**PAGE BY TAGS**

![tag-food](https://github.com/user-attachments/assets/ce017e28-fd46-4f70-af3c-a28eca5c54ba)


**PROFILE PAGE**
![profile](https://github.com/user-attachments/assets/10d87667-a201-4ae5-833d-6d7c85a7c765)



**POST_DETAIL PAGE**

![post-detail](https://github.com/user-attachments/assets/3d5857f6-628a-4933-9d9f-d1a3b1164986)

## Technologies Used!
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
