
import serial
import httplib
from urllib import urlencode

sequence = ''

def port_open():
    ser = serial.Serial(0)
    s = ser.read(12)
    return s

seq = port_open()
sequence = seq[1:]
print sequence
params = urlencode({'sequence':sequence,'place':'kannur','time':'12.00'})
headers = {"Content-Type":"application/x-www-form-urlencoded","Accept":"text/plain"}
conn = httplib.HTTPConnection("127.0.0.1:8080")
conn.request("POST","/",params,headers)

#response = conn.getresponse()
#print response.status,response.reason

