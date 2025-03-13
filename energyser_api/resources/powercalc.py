from flask_restful import Resource
from helpers.user import *
from helpers.property import *


class UserApi(Resource):
    def post(self, route):
        if route == "createuser":
            return CreateUser()
        
        if route == "loginuser":
            return LoginUser()

class PropertyApi(Resource): 
    def post(self, route):
        if route == "AddDeviceStore":
            return AddDeviceStore()
        
        if route == "AddDeviceHouse":
            return AddDeviceHouse()
        
        if route == "AddDeviceAgency":
            return AddDeviceAgency()
        
        if route == "AddDeviceCompany":
            return AddDeviceCompany()
    

    
    def get(self, route):
        if route == "AllStoreDevice":
            return AllStoreDevice()
        
        if route == "AllHouseDevice":
            return AllHouseDevice()
        
        if route == "AllAgencyDevice":
            return AllAgencyDevice() 
        
        if route == "AllCompanyDevice":
            return AllCompanyDevice()
        