import os
import platform
from pyuac import main_requires_admin


# TODO: create dns servers.json and load dns servers from json file

class dns_tools:

    @staticmethod
    def dns_query():
        # query the input url using scapy
        # use option for custom dns server
        pass

    @staticmethod
    @main_requires_admin
    def set_dns(dns_dict_object, interface):
        if platform.system() == "Windows":
            os.system("netsh interface ip set dns \"" + interface + "\" static " + dns_dict_object["primary"])
            if dns_dict_object["secondary"] != "null":
                os.system(
                    "netsh interface ip add dns \"" + interface + "\" " + dns_dict_object["secondary"] + " INDEX=2")
        else:
            raise Exception("Operating system not supported")

    @staticmethod
    @main_requires_admin
    def disable_dns(interface):
        if platform.system() == "Windows":
            os.system("netsh interface ip set dns \"" + interface + "\" source=dhcp")
        else:
            raise Exception("Operating system not supported")


class dns_storage_handling:

    @staticmethod
    def add_to_storage(dns_dict):
        pass
