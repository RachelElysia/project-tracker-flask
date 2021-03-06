"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import hackbright

app = Flask(__name__)
db = SQLAlchemy()

@app.route('/')
def homepage():
    """This is the homepage."""

    #QUERY 1: get all students
    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        """

    db_cursor = db.session.execute(QUERY)

    all_students = db_cursor.fetchall()
    print("\n\n\n\n*******")
    print(all_students)
    print("*****\n\n\n\n")

    #QUERY 2: get all projects

    QUERY = """
        SELECT title, description, max_grade
        FROM projects
        """

    db_cursor = db.session.execute(QUERY)

    all_projects = db_cursor.fetchall()
    print("\n\n\n\n*******")
    print(all_projects)
    print("*****\n\n\n\n")

    return render_template("homepage.html",
                            all_projects = all_projects,
                            all_students = all_students)

@app.route("/student")
def get_student():
    """Show information about a student."""

    # Step 2: Get github info from form on student-search
    github = request.args.get('github')

    print("*******\n\n", github )

    # Unpack student data from Hackbright.sql
    first, last, github = hackbright.get_student_by_github(github)
    print("*******\n\n", first )
    print("*******\n\n", last )
    print("*******\n\n", github )

    # Step 8?: Grab grade from student's github
    rows = hackbright.get_grades_by_github(github)
    # Returns rows

    # Step 3: render student_info passing through 3 variables to template
    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github,
                            rows=rows)
    return html

# THIS VIEW FUNCTION NEEDS TO LOOK SIMILAR TO FUNCTION AT LINE 13
# EXCEPT NO GET REQUESTS, SHOULD COME FROM LINK OF PROJECT INFO
@app.route("/student/<github>")
def project_to_student(github):
    """See a student from project page."""
    first, last, github = hackbright.get_student_by_github(github)
    

    # SIMILAR TO FUNCTION ON LINE 13
    rows = hackbright.get_grades_by_github(github)
    # Returns rows

    return render_template("student_info.html", 
                            first = first,
                            last = last,
                            github = github,
                            rows = rows)

@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student.""" 

    # Step 1: Create 3 variables to receive form information using request.form.get()
    last_name = request.form.get("last")
    first_name = request.form.get("first")
    github_name = request.form.get("github")

    # Skip Step 2-4 because it's in def make_new_student in hackbright.py
    hackbright.make_new_student(first_name, last_name, github_name)
    
    
    # Step 5: Return redirect
    return render_template("/student_added.html",
                    first = first_name,
                    last = last_name,
                    github = github_name)

@app.route("/student-create")
def create_a_student():
    """Show form for searching for a student."""

    return render_template("student_create.html")

# Added a form to search for a student record
@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/project-info/<title>")
# Need to pass in variable title into view function
# To use title in get_project_by_title
def view_project_info(title):
    #render_template("project-info.html", title, description, max_grade)
    # title = request.args.get(title)

    # Create variable holding tuple (title, description, grade)
    row = hackbright.get_project_by_title(title)


    # Step 10?: Create variable holding tuples of all students info
    # Iterate over on project-info
    all_grades = hackbright.get_grades_by_title(title)


    return render_template('project-info.html',
                            row = row,
                            all_grades = all_grades)

    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

#mine still works with , port=5000

#close server and browser
#restart both