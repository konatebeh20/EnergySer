from flask_restful import Resource
from flask import request
from helpers.property import *


class PropertiesApi(Resource):
    def post(self, route):
        if route == "add-property":
            return CreateProperties()

    #     if route == "getsingledevice":
    #         return GetSingleDevice()
        

    # def get(self, route):
    #     if route == "getalldevice":
    #         return GetAllDevice()
        

    # def patch(self, route):
    #     if route == "updatedevice":
    #         return UpdateDevice()
        
        
    # def delete(self, route):
    #     if route == "deletedevice":
    #         return DeleteDevice()

