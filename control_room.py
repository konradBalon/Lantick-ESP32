from machine import Pin, enable_irq, disable_irq
import utime
class Control_room:
    
    button_presses = 0 # the count of times the button has been pressed
    last_time = 0 # the last time we pressed the button 
    
    def http_get(self,url):
        import socket
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        auth = "YWRtaW46YWRtaW4wMA=="
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\nAuthorization: Basic %s\r\n\r\n' % (path, host, auth), 'utf8'))
#         while True:
#             data = s.recv(100)
#             if data:
#                 print(str(data, 'utf8'), end='')
#             else:
#                 break
        s.close()
    
    def callback(self,p):
        global button_presses, last_time
        new_time = utime.ticks_ms()
        
        if (new_time - self.last_time) > 300: 
            self.button_presses +=1
            self.last_time = new_time
            print('pin change', p, utime.localtime())
            self.http_get('http://192.168.0.115/stat.php?inv=1')

    def get_pin(self, gpio=15):

        pin = Pin(gpio, Pin.IN, Pin.PULL_UP)
        pin.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        print(pin.value())
    

    
