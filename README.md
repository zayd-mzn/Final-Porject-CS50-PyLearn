# PyLearn

#### Video Demo : https://www.youtube.com/watch?v=AfLQDKBy7OI

#### Description :

**PyLearn** is an interactive, web-based platform built to help users learn Python programming in a structured but flexible way. The project combines theory, hands-on coding, and progress tracking to create a learning experience that is both engaging and accessible. Unlike many static tutorials, PyLearn allows learners to write, run, and test Python code directly in their browser, without the need for local setup.  

This README describes in detail how the project works, the purpose of each file I wrote, the reasoning behind my design decisions, and the scope of its functionality. It’s a reflection of both the technical architecture and the thought process that guided its creation.

---

## Project Overview

The aim of PyLearn is to create an **all-in-one beginner-friendly learning platform** for Python that works seamlessly online. The application is built with **Flask (Python)** as the backend framework, **SQLite** for persistent storage, and **HTML/CSS/JavaScript** (with Bootstrap) for the frontend interface.  

PyLearn is organized into “lessons,” each of which contains an explanation of a topic, examples, and an interactive coding challenge. The system tracks user progress, so learners can pick up where they left off or jump around to topics they’re most interested in. Unlike linear-only tutorials, PyLearn supports **lesson order freedom**, a deliberate design choice explained later.

---

## File-by-File Breakdown

The repository is organized to follow Flask’s application structure, making it easy to maintain and extend.

### `main.py`
The application’s entry point. This file creates the Flask application instance by importing the `create_app()` function from the `website` package and running it. Keeping the run command separate from the app factory ensures cleaner code and easier testing.

### `website/__init__.py`
This file defines the **application factory function**, `create_app()`, which initializes the Flask app, configures the database, registers blueprints (`auth` and `views`), and sets up extensions like `Flask-Login` for authentication. Using the factory pattern improves modularity and flexibility.

### `website/models.py`
Defines the SQLAlchemy database models:
- **User** — Stores user credentials and login information.
- **Lesson** — Stores lesson titles and content.
- **UserProgress** — Tracks which lessons a user has completed.

This separation of concerns allows for easy addition of new models in the future without disrupting existing code.

### `website/views.py`
Contains all routes related to the **main content** of the platform. This includes:
- Home page
- Lessons list
- Lesson detail view
- Progress updates

The `@login_required` decorator is applied to most routes to ensure that only authenticated users can access lessons and save progress.

### `website/auth.py`
Handles user authentication:
- Registration (`/sign-up`)
- Login (`/login`)
- Logout (`/logout`)
It integrates with Flask-Login to manage session handling securely.

### `website/templates/`
This folder contains all the HTML templates, which use **Jinja2 templating** to dynamically render lesson content, progress indicators, and user data.

Key templates include:
- `base.html` — Master layout with navigation bar and placeholders for page-specific content.
- `home.html` — Displays a welcome message and quick access to lessons.
- `lessons.html` — Lists all available lessons with completion status.
- `lesson.html` — Displays the content of the first lesson and includes the interactive coding challenge.

### `requirements.txt`
Lists all Python dependencies needed to run the project, ensuring consistent installation across environments.

---

## Functionality

When a user logs in, or signs up, they can:
1. Browse the list of available lessons.
2. Open any lesson and read the provided explanation.
3. Submit their answer to the different exercices to get immediate feedback.
4. Have their progress saved automatically.

The progress tracking system uses the `UserProgress` table to store a Boolean flag for each lesson completion. This information is shown next to lesson titles so users can see what’s done and what’s pending.

---

## Future Improvements

While the current version of PyLearn is fully functional, there are several enhancements I plan to add:
- **Gamification:** Award badges and points for completed lessons.
- **More interactive platform:** Add a space to write some Python code and securely execute it.
- **Dark Mode:** Allow users to toggle between light and dark themes.
- **Expanded Curriculum:** Add advanced topics like object-oriented programming and web scraping.
- **Internationalization:** Offer lessons in multiple languages.

---

## Conclusion

PyLearn is more than just a coding tutorial — it’s an interactive environment that blends structured learning with the flexibility to explore. Every design choice was made to balance usability, scalability, and educational effectiveness.  

From the database models to the lesson templates, each part of the project contributes to a consistent, enjoyable learning experience. This README serves not only as technical documentation but also as a reflection of the care and intention behind the project’s creation.
