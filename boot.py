# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from wifi_connection import WifiConnection

con = WifiConnection('TP-Link_6BBF','granat12')
con.do_connect()

