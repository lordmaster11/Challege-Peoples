#!/usr/bin/env python3

from flask import Flask, render_template, request
from services import*
from services.service import create_people, get_peoples, get_people, delete_people, edit_people, get_courses

app = Flask(__name__)

@app.route('/')
def index():
    peoples = get_peoples()
    courses = get_courses()
    return render_template('index.html', peoples=peoples, courses=courses)

@app.route('/', methods= ['POST'])
def add_people():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        course = request.form['course']

        data = {"first_name": first_name,"last_name": last_name,"email": email,"courses": [{"id": course}]}

        #course1 = request.form['course1']
        #course2 = request.form['course2']
        #course3 = request.form['course3']

        #data = {"first_name": first_name,"last_name": last_name,"email": email,"courses": [{"id": course1}, {"id": course2}, {"id": course3}]}

        create_people(data)
        peoples = get_peoples() 
        courses = get_courses()  

    return render_template('index.html', peoples=peoples, courses=courses)

@app.route('/delete/<id>')
def delete(id):
    delete_people(id)
    peoples = get_peoples() 
    courses = get_courses()

    return render_template('index.html', peoples=peoples, courses=courses)

@app.route('/edit/<id>')    
def get_student(id):
    people = get_people(id)
    courses = get_courses()

    return render_template('edit.html', people=people, courses=courses)    

@app.route('/update/<id>', methods= ['POST'])
def update_people(id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        course = request.form['course']

        data = {"first_name": first_name, "last_name": last_name, "email": email, "courses": [{"id": course}]}

        #course1 = request.form['course1']
        #course2 = request.form['course2']
        #course3 = request.form['course3']

        #data = {"first_name": first_name, "last_name": last_name, "email": email, "courses": [{"id": course1}, {"id": course2}, {"id": course3}]}
        #data = {"first_name": first_name,"last_name": last_name,"email": email,"courses": []}
        edit_people(id, data)
        peoples = get_peoples() 
        courses = get_courses()

    return render_template('index.html', peoples=peoples, courses=courses) 

if __name__ == '__main__':
        app.run(debug=True)