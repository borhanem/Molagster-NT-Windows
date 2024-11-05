import ipaddress
import threading
import os
import json


def ipv4_subnet_address_extractor(ip, mask):
    mask_list = mask.split(".")
    ip_list = ip.split(".")
    net_list = [None] * 4
    for i in range(4):
        ip_field = int(ip_list[i])
        mask_field = int(mask_list[i])
        net_list[i] = ip_field & mask_field
    net_addr = ""
    for i in range(4):
        net_addr += str(net_list[i]) + '.'
    net_addr = net_addr[:-1]
    return net_addr

def ip_validator(input_str):
    try:
        ipaddress.ip_address(input_str)
        return True
    except:
        return False


def threaded(fn):
    def wrapper(*args, **kwargs):
        _thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        _thread.start()
        return _thread

    return wrapper


class json_io:
    # TODO: Check for duplicate entries in a json

    # Appends a dictionary object to json array
    @staticmethod
    def append_to_json(file_name, dict_object):
        if type(dict_object) == dict:
            with open(file_name, 'r') as jsoni:
                listobj = json.load(jsoni)
                listobj.append(dict_object)

            with open(file_name, 'w') as jsonw:
                json.dump(listobj, jsonw, indent=4, separators=(',', ': '))

    # Checks if json structure is an empty array
    @staticmethod
    def check_json_arr(file_name):
        jsoni = open(file_name, 'r')
        try:
            listobj = json.load(jsoni)
            if type(listobj) != list:  # Json array not present
                jsoni.close()
                os.remove(file_name)
                json_io.check_file(file_name)
        except:  # Unacceptable Json structure
            jsoni.close()
            os.remove(file_name)
            json_io.check_file(file_name)
        finally:
            jsoni.close()

    # Checks for healthy file
    @staticmethod
    def check_file(file_name):
        if os.path.isfile(file_name) is False:  # File doesn't exist
            with open(file_name, 'w') as jsonw:
                data = []
                json.dump(data, jsonw, indent=4)
        else:  # File exists but needs to get checked
            json_io.check_json_arr(file_name)

    @staticmethod
    def search_json(file_name, search_key, search_value):
        with open(file_name, 'r') as jsoni:
            listobj = json.load(jsoni)
            for dict_object in listobj:
                if dict_object[search_key] == search_value:
                    return dict_object
        return None

    @staticmethod
    def list_getter(file_name):
        with open(file_name, 'r') as jsoni:
            listobj = json.load(jsoni)
            return listobj
