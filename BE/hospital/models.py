from flask import Flask,jsonify
import uuid
from app import db

class Hospital:
    def create(self):
        hospital={
            "_id":"",
            "code":"",
            "name":"",
            "position":"",
            "description":""
        }
        return jsonify(hospital), 200
    
    def add(self,obj):
        if  'code' in obj and 'name' in obj and'position' in obj and'description' in obj  :
            # create a new hospital from the recieved data
            hospital={
            "_id":uuid.uuid4().hex,
            "code":obj['code'],
            "name":obj['name'],
            "position":obj['position'],
            "description":obj['description']
            }
            # chech if not existing name or code
            if db.hospitals.find_one({"name":hospital['name']}) or db.hospitals.find_one({"code":hospital['code']})  :
                return jsonify({"error":"Hospital name or code already used"}),400
            # insert the nesw hospital
            if db.hospitals.insert_one(hospital):
                return jsonify(hospital), 200

        return  jsonify({"error":"Hospital add failure"}),400
    
    def delete(self,obj) :
        if '_id' in obj :
            #  create a new hospital from the recieved data
            hospital={
            # "code":obj['code'],
            "_id":obj['_id'],
            # "position":obj['position'],
            # "description":obj['description']
            }
            
            if db.hospitals.find_one({"_id":hospital['_id']})  :
                db.hospitals.delete_one({"_id":hospital['_id']})
                return jsonify({"resp":"Hospital with ID : " + hospital['_id'] + " found and deleted"}),200

        return  jsonify({"error":"Hospital delete failure"}),400

    def update(self,obj) :
        if '_id' in obj :

            # if db.hospitals.find_one({"name":obj['name']}) or db.hospitals.find_one({"code":obj['code']})  :
            #     return jsonify({"error":"Hospital name or code already used"}),400

            if db.hospitals.find_one({"_id":obj['_id']})  :

                if 'description' in obj :
                    db.hospitals.update_one({"_id":obj['_id']},{"$set":{"description":obj['description']}}, upsert=False)

                if 'code' in obj :
                    if  db.hospitals.find_one({"code":obj['code']})  :
                        return jsonify({"error":"Hospital code already used"}),400
                    db.hospitals.update_one({"_id":obj['_id']},{"$set":{"code":obj['code']}}, upsert=False)

                if 'position' in obj :
                    db.hospitals.update_one({"_id":obj['_id']},{"$set":{"position":obj['position']}}, upsert=False)    

                if 'name' in obj :
                    if db.hospitals.find_one({"name":obj['name']})  :
                        return jsonify({"error":"Hospital name already used"}),400
                    db.hospitals.update_one({"_id":obj['_id']},{"$set":{"name":obj['name']}}, upsert=False)

                return jsonify(db.hospitals.find_one({"_id":obj['_id']})),200

            return  jsonify({"error":"Hospital update by name failure"}),400

    def all(self) :
        
        # list all the hospitals in the DB
        if db.hospitals.find({}) :
            resp=[]
            for i in db.hospitals.find({}):
                resp.append(i)
            return jsonify(resp) ,200

        return  jsonify({"error":"Nothing found"}),400

    def find_id(self,id) :

        if db.hospitals.find_one({"_id":id})  :
            return jsonify(db.hospitals.find_one({"_id":id}) ),200

        return  jsonify({"error":"No hospital found"}),400