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


# class Add_property(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     de_name = db.Column(db.String(128), nullable=False)
#     de_amperage = db.Column(db.String(128), nullable=False)
#     de_wattage = db.Column(db.String(128), nullable=False)
#     de_usage_time = db.Column(db.String(128), nullable=False)
#     de_usage_day = db.Column(db.String(128), nullable=False)
#     de_uid = db.Column(db.String(128), nullable=False)
#     de_property = db.Column(db.String(128), nullable=False)
#     creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
#     update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Properties(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    type_client = db.Column(db.String(50), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    property_name = db.Column(db.String(100), nullable=False)

    global_active_power = db.Column(db.Float, nullable=True)
    global_reactive_power = db.Column(db.Float, nullable=True)
    voltage = db.Column(db.Float, nullable=True)
    global_intensity = db.Column(db.Float, nullable=True)
    sub_metering_1 = db.Column(db.Float, nullable=True)
    sub_metering_2 = db.Column(db.Float, nullable=True)
    sub_metering_3 = db.Column(db.Float, nullable=True)

    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Property {self.property_name}>'

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # de_name = db.Column(db.String(128), nullable=False)
    # de_amperage = db.Column(db.String(128), nullable=False)
    # de_wattage = db.Column(db.String(128), nullable=False)
    # de_usage_time = db.Column(db.String(128), nullable=False)
    # de_usage_day = db.Column(db.String(128), nullable=False)
    # de_uid = db.Column(db.String(128), nullable=False)
    # de_property = db.Column(db.String(128), nullable=False)
    # creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    # update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class recommander(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    recommander = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    property = db.relationship('Properties', back_populates='recommanders')

Properties.recommanders = db.relationship('recommander', back_populates='property')