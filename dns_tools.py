import os
import platform
import sys

import helper_module as helper
from pyuac import main_requires_admin
from scapy.all import *
import socket
import subprocess


# TODO : fix admin problems
# TODO: create dns servers.json and load dns servers from json file
# TODO: implement dns_query & showinterfaces
class dns_tools:
    @staticmethod
    def dns_query():
        pass

    @staticmethod
    @main_requires_admin
    def showinterfaces():
        pass

    @staticmethod
    @main_requires_admin
    def set_dns(dns_dict_object, interface):
        if sys.platform == "win32":
            command = "netsh interface ip set dns \"" + interface + "\" static " + dns_dict_object["primary"]
            os.system(command)
            if dns_dict_object["secondary"] != "null":
                secondary_command = "netsh interface ip add dns \"" + interface + "\" " + dns_dict_object[
                    "secondary"] + " INDEX=2"
                os.system(secondary_command)
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
