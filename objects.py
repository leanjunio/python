class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Name:" + self.name + " Age: " + str(self.age))

personOne = Person("John", 20)
personTwo = Person("Sally", 21)
personThree = Person("Rob", 22)

personOne.details()
personTwo.details()
personThree.details()

class Server:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
    
    def setHostname(self, hostname):
        self.hostname = hostname


    def setIp(self, ip):
        self.ip = ip
        
    def getHostname(self):
        return self.hostname

    def getIp(self):
        return self.ip

    def info(self):
        return "Server - Hostname: " + self.hostname + " IP: " + self.ip
    
google = Server('Google', '234.1.162.77')
microsoft = Server('Microsoft', '234.1.162.77')
dropbox = Server('DropBox', '155.80.106.239')

print(google.info())
print(microsoft.info())
print(dropbox.info())

