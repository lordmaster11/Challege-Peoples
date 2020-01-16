#!/usr/bin/env python3

import requests
import json

def get_json(url):
    response = requests.get(url)

    if response.status_code == 200:
        response_json = json.loads(response.text)

        return response_json

def get_peoples():
    url = 'http://jdicostanzo.challenge.trinom.io/api/peoples'
    response = get_json(url)
    peoples = []

    for people in response['data']:
        peoples.append(people) 

    return peoples

def get_courses():
    url = 'http://jdicostanzo.challenge.trinom.io/api/courses'
    response = get_json(url)
    courses = []

    for course in response:
        courses.append(course) 

    return courses

def get_people(id):
    url = 'http://jdicostanzo.challenge.trinom.io/api/peoples/' + str(id)
    response = get_json(url)

    return response

def create_people(params):    
    url = 'http://jdicostanzo.challenge.trinom.io/api/peoples'

    response = requests.post(
            url=url, 
            headers={'Content-Type': 'application/json'},
            data=json.dumps(params),
        )
    return response

def delete_people(params):
    url = 'http://jdicostanzo.challenge.trinom.io/api/peoples/' + params
    response = requests.delete(url)

    return response
    
def edit_people(id, params):
    url = 'http://jdicostanzo.challenge.trinom.io/api/peoples/' + id

    response = requests.put(
            url=url, 
            headers={'Content-Type': 'application/json'},
            data=json.dumps(params),
        )

    return response

def people_exist(params):
    res= False
    for people in get_peoples():
        if people['email'] == params:
            res = True
    return res      
