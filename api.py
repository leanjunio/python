from socket import gethostbyname

class Server:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = gethostbyname(hostname)

    def getIP(self):
        return "HostName: " + self.hostname + " IP Address: " + self.ip


google = Server('google.com')
apotex = Server('apotex.ca')
toyota = Server('toyota.ca')

print(google.getIP())
print(apotex.getIP())
print(toyota.getIP())
