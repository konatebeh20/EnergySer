import datetime
import pymysql
from config.db import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_fullname = db.Column(db.String(128), nullable=False)
    ad_username = db.Column(db.String(128), nullable=False)
    ad_mobile = db.Column(db.String(128), nullable=False)
    ad_address = db.Column(db.String(128), nullable=False)
    ad_email = db.Column(db.String(128), nullable=False)
    ad_password = db.Column(db.String(128), nullable=False)
    ad_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    de_name = db.Column(db.String(128), nullable=False)
    de_amperage = db.Column(db.String(128), nullable=False)
    de_wattage = db.Column(db.String(128), nullable=False)
    de_usage_time = db.Column(db.String(128), nullable=False)
    de_usage_day = db.Column(db.String(128), nullable=False)
    de_uid = db.Column(db.String(128), nullable=False)
    de_property = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    de_name = db.Column(db.String(128), nullable=False)
    de_amperage = db.Column(db.String(128), nullable=False)
    de_wattage = db.Column(db.String(128), nullable=False)
    de_usage_time = db.Column(db.String(128), nullable=False)
    de_usage_day = db.Column(db.String(128), nullable=False)
    de_uid = db.Column(db.String(128), nullable=False)
    de_property = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    de_name = db.Column(db.String(128), nullable=False)
    de_amperage = db.Column(db.String(128), nullable=False)
    de_wattage = db.Column(db.String(128), nullable=False)
    de_usage_time = db.Column(db.String(128), nullable=False)
    de_usage_day = db.Column(db.String(128), nullable=False)
    de_uid = db.Column(db.String(128), nullable=False)
    de_property = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    de_name = db.Column(db.String(128), nullable=False)
    de_amperage = db.Column(db.String(128), nullable=False)
    de_wattage = db.Column(db.String(128), nullable=False)
    de_usage_time = db.Column(db.String(128), nullable=False)
    de_usage_day = db.Column(db.String(128), nullable=False)
    de_uid = db.Column(db.String(128), nullable=False)
    de_property = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)