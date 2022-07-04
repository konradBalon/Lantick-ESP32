
class WifiConnection:
# works only with WiFi 2.4 GHz

    essid = '<name of your wifi access point >'
    password = '<wifi password>'

    def __init__(self, essid, password):
        self.essid = "TP-Link_6BBF"
        self.password = "granat12"


    def do_connect(self):
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(self.essid, self.password)
            while not wlan.isconnected():
                pass
        print('network config:', wlan.ifconfig())
    
    def http_get(self,url):
        import socket
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'), end='')
            else:
                break
        s.close()    
