import ipaddress
import threading
import os
import json


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
    @staticmethod
    def append_to_json(dict_object, file_name):
        if type(dict_object) == dict:
            with open(file_name) as jsoni:
                listobj = json.load(jsoni)
                listobj.append(dict_object)

            with open(file_name, 'w') as jsonw:
                json.dump(listobj, jsonw, indent=4, separators=(',', ': '))

    @staticmethod
    def check_file_exists(file_name):
        if os.path.isfile(file_name) is False:
            f = open(file_name, 'w')
            f.close()

