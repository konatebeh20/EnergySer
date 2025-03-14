from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db        

import bcrypt
from flask_jwt_extended import create_access_token
from model.energyser import *


def CreateProperties():
    reponse = {}

    try:
        # ad_fullname = (request.json.get('fullname'))
        # ad_username = (request.json.get('username'))
        # ad_mobile = (request.json.get('mobile'))      
        addresse = request.json.get('adresse')
        email = request.json.get('email')
        propertyName = request.json.get('property_name')
        propertyType = request.json.get('property_type')
        typeClient = request.json.get('type_client')
        # uid = str(uuid.uuid4())
       
        
        new_property = Properties()
        # new_admin.fullname = fullname 
        # new_admin.username = username
        # new_admin.mobile = mobile
        new_property.adresse = addresse
        new_property.email = email
        new_property.property_name = propertyName
        new_property.property_type = propertyType
        new_property.type_client = typeClient
        
        # new_admin.uid = ad_uid
        
        db.session.add(new_property)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse