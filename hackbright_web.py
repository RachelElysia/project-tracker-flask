"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # Step 2: Get github info from form on student-search
    github = request.args.get('github')

    # Unpack student data from Hackbright.sql
    first, last, github = hackbright.get_student_by_github(github)

    # Step 3: render student_info passing through 3 variables to template
    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github)
    return html

# Added a form to search for a student record
@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")
    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

#mine still works with , port=5000

#close server and browser
#restart both