
try:
    import subprocess
    from ipaddress import ip_address

    class IP_Live:
        def __init__(self, ip, start, end):
            self.ip = ip
            self.start_host = start
            self.end_host = end

        def ip_cutting(self, ip):
            new_ip = ''
            ip = ip.split(".")      #spliting IP address into 4 part
            new_ip = ".".join(ip[:-1])      # keeping only first three part of the given ip address

            return new_ip


        def ip_validation(self):
            valid_ips = []
            if ip_address(self.ip):     # checking the validation of the IP   
                for i in range(self.start_host, self.end_host+1):
                    new_ip = self.ip_cutting(self.ip)       # last octet remove function
                    valid_ips.append(new_ip+"."+str(i))     # listing valid IP addresses adding by host in last octet
                return valid_ips
            else:
                print(self.ip, " is bang")

        # Function for Pinging the valied ip addresses.
        def ping_ip(self):
            for i in self.ip_validation():
                var = (subprocess.run("ping {}".format(i), 1, shell=True,))     # ping comand with subprocess module
                if var.returncode == 0:
                    print("\n\tIP address {} is alive.".format(i))
                else:
                    print("\n\tIP address {} is dead.")



    if __name__ == "__main__":
        first = input("Enter your IP address: ")
        host1 = int(input("Enter Start host: "))
        host2 = int(input("Enter End host: "))
        obj = IP_Live(first, host1, host2)      # Creating object of class
        obj.ping_ip()               # Calling the func

except Exception as e:
    print("You are getting this ERROR: {}".format(e))
