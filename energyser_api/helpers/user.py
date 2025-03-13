from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db        

import bcrypt
from flask_jwt_extended import create_access_token
from model.powercalc import User


def CreateUser():
    reponse = {}

    try:
        ad_fullname = (request.json.get('fullname'))
        ad_username = (request.json.get('username'))
        ad_mobile = (request.json.get('mobile'))      
        ad_address = (request.json.get('address'))
        ad_email = (request.json.get('email'))
        ad_password = (request.json.get('password'))
        ad_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(ad_password.encode('utf-8'), bcrypt.gensalt())
        
        new_admin = User()
        new_admin.ad_fullname = ad_fullname 
        new_admin.ad_username = ad_username
        new_admin.ad_mobile = ad_mobile
        new_admin.ad_address = ad_address
        new_admin.ad_email = ad_email
        new_admin.ad_password = hashed_password
        new_admin.ad_uid = ad_uid
        
        db.session.add(new_admin)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse



def LoginUser():
    reponse = {}
    reponses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_admin = User.query.filter_by(ad_username=username).first()

        if login_admin and bcrypt.checkpw(password.encode('utf-8'), login_admin.ad_password.encode('utf-8')):
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=username)

            reponse['status'] = 'success'
            reponse['message'] = 'Login successful'
            # reponse['access_token'] = access_token

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid username or password'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse