import ipaddress
import threading

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
