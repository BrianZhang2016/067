from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from __init__ import db
from crud2.model import Subjects, Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud1 = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud1)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def subjects_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Subjects.query.all()]


def subjects_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Subjects.query.filter((Subjects.className.ilike(term)) | (Subjects.teacher.ilike(term)) | (Subjects.link.ilike(term)) | (Subjects.studentsEnrolled.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def subject_by_id(classID):
    """finds User in table matching userid """
    return Subjects.query.filter_by(classID=classID).first()


# User extraction from SQL
def subject_by_teacher(teacher):
    """finds User in table matching email """
    return Subjects.query.filter_by(teacher=teacher).first()


""" app route section """


# Default URL
@app_crud1.route('/')
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=subjects_all())


# CRUD create/add
@app_crud1.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Subjects(
            request.form.get("className"),
            request.form.get("teacher"),
            request.form.get("link"),
            request.form.get("studentsEnrolled")
        )
        po.create()
    return redirect(url_for('crud.crud'))


# CRUD read
@app_crud1.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        classID = request.form.get("classID")
        po = subject_by_id(classID)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@app_crud1.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        classID = request.form.get("classID")
        teacher = request.form.get("teacher")
        link = request.form.get("link")
        studentsEnrolled = request.form.get("studentsEnrolled")
        po = subject_by_id(classID)
        if po is not None:
            po.update(teacher)
            po.update(link)
            po.update(studentsEnrolled)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_crud1.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        classID = request.form.get("classID")
        po = subject_by_id(classID)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@app_crud1.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("search.html")

@app_crud1.route('/enroll/')
def enroll():
    return render_template("enroll.html")


# Search request and response
@app_crud1.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(subjects_ilike(term)), 200)
    return response





