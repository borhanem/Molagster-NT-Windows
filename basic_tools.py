import socket
from urllib.request import urlopen
import re as r


class network_tools:

    @staticmethod
    def get_private_ip_hostname():
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        result = (host_name, ip_address)
        return result

    @staticmethod
    def get_public_ip():
        d = str(urlopen('http://checkip.dyndns.com/')
                .read())

        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

