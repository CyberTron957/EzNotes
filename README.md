# EzNotes

EzNotes is a web-based notes application built with Django and SQLite. It allows users to create, edit, and delete notes. The application features a clean and responsive user interface using Bootstrap, and it supports user authentication for secure access to personal notes.

## Features

- User authentication (login and logout)
- Create, edit, and delete notes
- Responsive UI using Bootstrap
- Real-time synchronization across devices

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/CyberTron957/EzNotes.git
cd EzNotes

Set Up the Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

Apply Migrations

bash

python manage.py makemigrations
python manage.py migrate

Create a Superuser

bash

python manage.py createsuperuser

Run the Development Server

bash

python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/ to access the application.
Usage

    Register for an account or log in with an existing account.
    Create, edit, and delete your notes.
    Notes are private and accessible only to the logged-in user.

Project Structure

markdown

EzNotes/
├── notes/
│   ├── migrations/
│   ├── static/
│   │   └── notes/
│   │       └── css/
│   │           └── styles.css
│   ├── templates/
│   │   └── notes/
│   │       ├── add_note.html
│   │       └── index.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── custom_filters.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── EzNotes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md

Custom Filters

The project includes a custom template filter to add CSS classes to form fields.
Custom Filter Usage

    Create the templatetags directory:

    sh

mkdir -p notes/templatetags
touch notes/templatetags/__init__.py

Create the custom filter file (notes/templatetags/custom_filters.py):

python

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

Load the custom filter in your template (add_note.html):

html

    {% load custom_filters %}
    {{ form.content|add_class:"form-control" }}

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Django Framework
    Bootstrap

Contact

For any inquiries, please reach out to [yourname@example.com].