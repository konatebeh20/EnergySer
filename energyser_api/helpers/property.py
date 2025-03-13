from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db        

import bcrypt
from flask_jwt_extended import create_access_token
from model.powercalc import *


def AddDeviceStore():
    reponse = {}

    try:
        de_name = (request.json.get('de_name'))
        de_amperage = (request.json.get('de_amperage'))      
        de_wattage = (request.json.get('de_wattage'))
        de_usage_time = (request.json.get('de_usage_time'))
        de_usage_day = (request.json.get('de_usage_day'))
        de_property = 'Store'
        de_uid = str(uuid.uuid4())
        
        new_device = Store()
        new_device.de_name = de_name
        new_device.de_amperage = de_amperage
        new_device.de_wattage = de_wattage
        new_device.de_usage_time = de_usage_time
        new_device.de_usage_day = de_usage_day
        new_device.de_property = de_property
        new_device.de_uid = de_uid
        
        db.session.add(new_device)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse


def AddDeviceHouse():
    reponse = {}

    try:
        de_name = (request.json.get('de_name'))
        de_amperage = (request.json.get('de_amperage'))      
        de_wattage = (request.json.get('de_wattage'))
        de_usage_time = (request.json.get('de_usage_time'))
        de_usage_day = (request.json.get('de_usage_day'))
        de_property = 'House'
        de_uid = str(uuid.uuid4())
        
        new_device = House()
        new_device.de_name = de_name
        new_device.de_amperage = de_amperage 
        new_device.de_wattage = de_wattage
        new_device.de_usage_time = de_usage_time
        new_device.de_usage_day = de_usage_day
        new_device.de_property = de_property
        new_device.de_uid = de_uid
        
        db.session.add(new_device)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse


def AddDeviceAgency():
    reponse = {}

    try:
        de_name = (request.json.get('de_name'))
        de_amperage = (request.json.get('de_amperage'))      
        de_wattage = (request.json.get('de_wattage'))
        de_usage_time = (request.json.get('de_usage_time'))
        de_usage_day = (request.json.get('de_usage_day'))
        de_property = 'Agency'
        de_uid = str(uuid.uuid4())
        
        new_device = Agency()
        new_device.de_name = de_name
        new_device.de_amperage = de_amperage
        new_device.de_wattage = de_wattage
        new_device.de_usage_time = de_usage_time
        new_device.de_usage_day = de_usage_day
        new_device.de_property = de_property
        new_device.de_uid = de_uid
        
        db.session.add(new_device)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse


def AddDeviceCompany():
    reponse = {}

    try:
        de_name = (request.json.get('de_name'))
        de_amperage = (request.json.get('de_amperage'))      
        de_wattage = (request.json.get('de_wattage'))
        de_usage_time = (request.json.get('de_usage_time'))
        de_usage_day = (request.json.get('de_usage_day'))
        de_property = 'Company'
        de_uid = str(uuid.uuid4())
        
        new_device = Company()
        new_device.de_name = de_name
        new_device.de_amperage = de_amperage
        new_device.de_wattage = de_wattage
        new_device.de_usage_time = de_usage_time
        new_device.de_usage_day = de_usage_day
        new_device.de_property = de_property
        new_device.de_uid = de_uid
        
        db.session.add(new_device)
        db.session.commit()

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse


def AllStoreDevice():
    response = {}
    time_device_used = 0
    wa_device_used = 0
    device_invoice = 0
    invoice = 0
    all_device_invoice = []
    
    try:
        all_devices = Store.query.all()

        devices_info = []

        for devices  in all_devices:

            de_usage_time = int(''.join(filter(str.isdigit, devices.de_usage_time)))
            de_usage_day = int(''.join(filter(str.isdigit, devices.de_usage_day)))
            de_wattage = int(''.join(filter(str.isdigit, devices.de_wattage)))

            time_device_used = de_usage_time * de_usage_day
            print('Time device used: ', time_device_used)

            wa_device_used = time_device_used * de_wattage
            Wa_device_used = wa_device_used / 1000
            print('Wattage device used: ', Wa_device_used, 'Kwh')

            device_invoice = round(Wa_device_used * 80)
            print('Device invoice: ', device_invoice)

            all_device_invoice.append(device_invoice)
            invoice = sum(all_device_invoice)
            
            devices_infos = {
                'de_name': devices.de_name,              
                'de_amperage': devices.de_amperage,              
                'de_wattage': devices.de_wattage,              
                'de_usage_time': devices.de_usage_time,              
                'de_usage_day': devices.de_usage_day, 
                'de_property': devices.de_property,             
                'de_uid': devices.de_uid, 
                'device_invoice': device_invoice    
            }
            devices_info.append(devices_infos)

            

        response['status'] = 'success'
        response['devices_info'] = devices_info
        # response['device_invoice'] = device_invoice
        response['total_invoice'] = invoice

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def AllHouseDevice():
    response = {}
    time_device_used = 0
    wa_device_used = 0
    device_invoice = 0
    all_device_invoice = []
    
    try:
        all_devices = House.query.all()

        devices_info = []

        for devices  in all_devices:

            de_usage_time = int(''.join(filter(str.isdigit, devices.de_usage_time)))
            de_usage_day = int(''.join(filter(str.isdigit, devices.de_usage_day)))
            de_wattage = int(''.join(filter(str.isdigit, devices.de_wattage)))

            time_device_used = de_usage_time * de_usage_day
            print('Time device used: ', time_device_used)

            wa_device_used = time_device_used * de_wattage
            Wa_device_used = wa_device_used / 1000
            print('Wattage device used: ', Wa_device_used, 'Kwh')

            device_invoice = round(Wa_device_used * 80)
            print('Device invoice: ', device_invoice)

            all_device_invoice.append(device_invoice)
            invoice = sum(all_device_invoice)
            
            devices_infos = {
                'de_name': devices.de_name,              
                'de_amperage': devices.de_amperage,              
                'de_wattage': devices.de_wattage,              
                'de_usage_time': devices.de_usage_time,              
                'de_usage_day': devices.de_usage_day, 
                'de_property': devices.de_property,             
                'de_uid': devices.de_uid, 
                'device_invoice': device_invoice    
            }
            devices_info.append(devices_infos)
            

        response['status'] = 'success'
        response['devices_info'] = devices_info
        # response['device_invoice'] = device_invoice
        response['total_invoice'] = invoice

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def AllAgencyDevice():
    response = {}
    time_device_used = 0
    wa_device_used = 0
    device_invoice = 0
    all_device_invoice = []
    
    try:
        all_devices = Agency.query.all()

        devices_info = []

        for devices  in all_devices:

            de_usage_time = int(''.join(filter(str.isdigit, devices.de_usage_time)))
            de_usage_day = int(''.join(filter(str.isdigit, devices.de_usage_day)))
            de_wattage = int(''.join(filter(str.isdigit, devices.de_wattage)))

            time_device_used = de_usage_time * de_usage_day
            print('Time device used: ', time_device_used)

            wa_device_used = time_device_used * de_wattage
            Wa_device_used = wa_device_used / 1000
            print('Wattage device used: ', Wa_device_used, 'Kwh')

            device_invoice = round(Wa_device_used * 80)
            print('Device invoice: ', device_invoice)

            all_device_invoice.append(device_invoice)
            invoice = sum(all_device_invoice)
            
            devices_infos = {
                'de_name': devices.de_name,              
                'de_amperage': devices.de_amperage,              
                'de_wattage': devices.de_wattage,              
                'de_usage_time': devices.de_usage_time,              
                'de_usage_day': devices.de_usage_day, 
                'de_property': devices.de_property,             
                'de_uid': devices.de_uid, 
                'device_invoice': device_invoice    
            }
            devices_info.append(devices_infos)
            

        response['status'] = 'success'
        response['devices_info'] = devices_info
        # response['device_invoice'] = device_invoice
        response['total_invoice'] = invoice

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def AllCompanyDevice():
    response = {}
    time_device_used = 0
    wa_device_used = 0
    device_invoice = 0
    all_device_invoice = []
    
    try:
        all_devices = Company.query.all()

        devices_info = []

        for devices  in all_devices:

            de_usage_time = int(''.join(filter(str.isdigit, devices.de_usage_time)))
            de_usage_day = int(''.join(filter(str.isdigit, devices.de_usage_day)))
            de_wattage = int(''.join(filter(str.isdigit, devices.de_wattage)))

            time_device_used = de_usage_time * de_usage_day
            print('Time device used: ', time_device_used)

            wa_device_used = time_device_used * de_wattage
            Wa_device_used = wa_device_used / 1000
            print('Wattage device used: ', Wa_device_used, 'Kwh')

            device_invoice = round(Wa_device_used * 80)
            print('Device invoice: ', device_invoice)

            all_device_invoice.append(device_invoice)
            invoice = sum(all_device_invoice)
            
            devices_infos = {
                'de_name': devices.de_name,              
                'de_amperage': devices.de_amperage,              
                'de_wattage': devices.de_wattage,              
                'de_usage_time': devices.de_usage_time,              
                'de_usage_day': devices.de_usage_day, 
                'de_property': devices.de_property,             
                'de_uid': devices.de_uid, 
                'device_invoice': device_invoice    
            }
            devices_info.append(devices_infos)
            

        response['status'] = 'success'
        response['devices_info'] = devices_info
        # response['device_invoice'] = device_invoice
        response['total_invoice'] = invoice

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


# def GenerateInvoice():
#     response = {}

#     try:
#         type = (request.json.get('type'))

#         if type == 'store':
#             store_property = AllStoreDevice()
#             Store_property = store_property['device_invoice']
#             invoice = sum(Store_property)
#             print(invoice)

#         if type == 'House':
#             store_property = AllHouseDevice()
#             Store_property = store_property['device_invoice']
#             invoice = sum(Store_property)
#             print(invoice)

#         if type == 'Agency':
#             store_property = AllAgencyDevice()
#             Store_property = store_property['device_invoice']
#             invoice = sum(Store_property)
#             print(invoice)

#         if type == 'Company':
#             store_property = AllCompanyDevice()
#             Store_property = store_property['device_invoice']
#             invoice = sum(Store_property)
#             print(invoice)

#         response['status'] = 'success'
#         response['total_invoice'] = invoice

#     except Exception as e:
#         response['status'] = 'error'
#         response['error_description'] = str(e)

#     return response