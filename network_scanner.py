import scapy.all as scapy


class Arp_Scan:

    @staticmethod
    def scan(ip):  # change to scan subnet
        arp_req_frame = scapy.ARP(pdst=ip)

        broadcast_ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

        answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
        print(answered_list)
        # print(150 * '_')
        # print(type(answered_list))
        result = []
        for i in range(0, len(answered_list)):
            # print(answered_list[i])
            client_dict = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
            result.append(client_dict)

        Arp_Scan.display_result(result)

    @staticmethod
    def display_result(result):
        for element in result:
            print(f"IP: {element['ip']} MAC: {element['mac']}")


class Port_Scan:
    @staticmethod
    def scan_tcp_port(ip, port):
        # bool return port existence
        # syn scan or what
        pass

    @staticmethod
    def scan_device(ip):
        # scans all ports using a for loop
        # returns a list or sth
        pass

    @staticmethod
    def scan_device_intense(ip):
        pass

    @staticmethod
    def display_result(result):
        pass
