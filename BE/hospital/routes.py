from flask import Flask, request

from app import app

from hospital.models import Hospital

@app.route('/hospital/',methods=['GET'])
def create():
    return Hospital().create()

@app.route('/hospital/add',methods=['POST'])
def add():
    resp   =Hospital().add(request.json)
    return resp

@app.route('/hospital/delete',methods=['POST'])
def delete():
    resp   = Hospital().delete(request.json)
    return resp

@app.route('/hospital/update',methods=['POST'])
def update():
    resp   = Hospital().update(request.json)
    return resp

@app.route('/hospital/all',methods=['GET'])
def all():
    resp   = Hospital().all()
    return resp
@app.route('/hospital/find_id/<Hosp_id>')
def find_id(Hosp_id):
    resp   = Hospital().find_id(Hosp_id)
    return resp