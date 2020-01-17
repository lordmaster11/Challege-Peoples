#!/usr/bin/env python3

from flask import Flask, render_template, request, flash, redirect, url_for
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
    try:
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            course = request.form['course']
            data = {"first_name": first_name,"last_name": last_name,"email": email,"courses": [{"id": course}]}
            
            if not people_exist(email):
                if first_name == "" or last_name == "" or email == "":
                    flash('Complete todos los datos')
                    return redirect(url_for('index'))
                else:    
                    create_people(data)
                    peoples = get_peoples() 
                    courses = get_courses()  
                    flash('Alumno inscripto') 
                    return render_template('index.html', peoples=peoples, courses=courses, len_peoples=len(get_peoples()))   
            else:
                if first_name == "" or last_name == "" or email == "":
                    flash('Complete todos los datos')
                    return redirect(url_for('index'))         
                else: 
                    flash('El alumno ya existe')
                    return redirect(url_for('index'))         

    except (KeyError):
        flash('Complete todos datos')
        return redirect(url_for('index'))

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
    course = course_people(id)

    return render_template('edit.html', people=people, courses=courses, len_peoples=len(get_peoples()), course=course)    

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
        
    return course    

@app.route('/data/<id>')
def data_people(id):
    people = get_people(id)
    peoples = get_peoples() 
    courses = get_courses()
    course = course_people(id)

    return render_template('data.html', people=people, peoples=peoples, courses=courses, len_peoples=len(get_peoples()), course=course) 

if __name__ == '__main__':
        app.run(debug=True)