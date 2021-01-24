"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy

# Step 1: Import hackbright database
import hackbright 

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_grades_by_github(github):
    """Get a list of all grades for a student by their github username"""

    QUERY = """
        SELECT project_title, grade
        FROM grades
        WHERE student_github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    rows = db_cursor.fetchall()

    for row in rows:
        print(f"Student {github} received grade of {row[1]} for {row[0]}")

    return rows




def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            github = args[0]
            get_student_by_github(github)

        elif command == "new_student":
            first_name, last_name, github = args  # unpack!
            make_new_student(first_name, last_name, github)

        elif command == "project":
            title = args[0]
            get_project_by_title(title)

        elif command == "grade":
            github, title = args
            get_grade_by_github_title(github, title)

        elif command == "assign_grade":
            github, title, grade = args
            assign_grade(github, title, grade)

        elif command == "student_grades":
            github = args[0]
            get_grades_by_github(github)

        elif command == "project_grades":
            title = args[0]
            get_grades_by_title(title)


if __name__ == "__main__":
    connect_to_db(app)

    handle_input()

    # To be tidy, we'll close our database connection -- though, since this
    # is where our program ends, we'd quit anyway.

    db.session.close()
