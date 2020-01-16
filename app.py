#!/usr/bin/env python3

from flask import Flask, render_template, request, flash
from services import*
from services.service import create_people, get_peoples, get_people, delete_people, edit_people, get_courses, people_exist

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    peoples = get_peoples()
    courses = get_courses()
    return render_template('index.html', peoples=peoples, courses=courses, len_peoples=len(get_peoples()))

@app.route('/', methods= ['GET','POST'])
def add_people():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        course = request.form['course']

        data = {"first_name": first_name,"last_name": last_name,"email": email,"courses": [{"id": course}]}
        
        if not people_exist(email):
            create_people(data)
            flash('Alumno inscripto')

            peoples = get_peoples() 
            courses = get_courses()   
        else:
            peoples = get_peoples() 
            courses = get_courses()  
            flash('El alumno ya existe')    

        return render_template('index.html', peoples=peoples, courses=courses, len_peoples=len(get_peoples()))   

@app.route('/delete/<id>')
def delete(id):
    delete_people(id)

    flash('Alumno eliminado')

    peoples = get_peoples() 
    courses = get_courses()

    return render_template('index.html', peoples=peoples, courses=courses, len_peoples=len(get_peoples()))

@app.route('/edit/<id>')    
def get_student(id):
    people = get_people(id)
    courses = get_courses()

    return render_template('edit.html', people=people, courses=courses, len_peoples=len(get_peoples()))    

@app.route('/update/<id>', methods= ['POST'])
def update_people(id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        course = request.form['course']

        data = {"first_name": first_name, "last_name": last_name, "email": email, "courses": [{"id": course}]}

        edit_people(id, data)
        
        flash('Alumno actualizado')

        peoples = get_peoples() 
        courses = get_courses()

    return render_template('index.html', peoples=peoples, courses=courses, len_peoples=len(get_peoples())) 

def course_people(id):
    people = get_people(id)

    for cour in people['courses']:
        course = cour
        print(cour, 'oursss')
    return course    

@app.route('/data/<id>')
def data_people(id):
    people = get_people(id)
    peoples = get_peoples() 
    courses = get_courses()
    course = course_people(id)

    #for course in people['courses']:
     #   return course

    return render_template('data.html', people=people, peoples=peoples, courses=courses, len_peoples=len(get_peoples()), course=course) 

if __name__ == '__main__':
        app.run(debug=True)