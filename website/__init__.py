from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "zayd"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Lesson, UserProgress
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    with app.app_context():
        if Lesson.query.count() == 0:
            lesson = Lesson(
                title="Introduction to Python",
                content="""Welcome to the first lesson! Here we learn about Python basics.
1. What is Python?
Python is a high-level, interpreted programming language known for its simplicity -its syntax is close to plain English-, 
versatility –used in web development, data science, AI, automation,..., community support –many libraries and frameworks to
help you build faster.

2. Why Learn Python?
Easy to learn for beginners. Powerful enough for professionals. Cross-platform (works on Windows, macOS, Linux).
Huge job market demand.

3. Your First Python Program
In Python, printing text is as simple as:

print("Hello, world!")

How it works:
print() is a built-in function that displays output on the screen. Text is written inside quotes " ".

4. Python Basics
Variables : Variables store information in memory.

name = "Alice"
age = 20

Name is a string ("Alice"). Age is an integer (20).

Data Types : Common Python data types:
str → "Hello"
int → 42
float → 3.14
bool → True / False

5. Comments
Comments are ignored by Python and used to explain code.

# This is a comment

6. Basic Math in Python

x = 10
y = 3
print(x + y)  # Addition → 13
print(x - y)  # Subtraction → 7
print(x * y)  # Multiplication → 30
print(x / y)  # Division → 3.333...
print(x // y) # Floor division → 3
print(x % y)  # Modulus → 1

7. Next Steps
After learning the basics, you’ll explore:
Conditionals (if, else)
Loops (for, while)
Functions
Modules and Libraries...""",
                category="Programming"
            )
            db.session.add(lesson)
            db.session.commit()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        app.app_context().push()
        db.create_all()
