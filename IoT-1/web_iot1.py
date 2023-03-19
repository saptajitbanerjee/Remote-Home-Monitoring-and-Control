import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import smtplib
from http.server import BaseHTTPRequestHandler, HTTPServer

smtpUser='jcomponentrasberrypibot@gmail.com'
smtpPass='waumkjgbiebmgmua'
send = 'Welcome User'
toAdd='saptajitbanerjee2002@gmail.com'
fromAdd = smtpUser

subject='Sending Email using Python'
header='To:'+toAdd+'\n'+'From:'+fromAdd+'\n'+'Subject:'+subject
body='From Python Program sending email'

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,0)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
Request = None
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    global send
    messagetosend = bytes(send,"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == 'on_1':
      GPIO.output(5,True)
    if Request == 'off_1':
      GPIO.output(5,False)
    if Request == 'on_2':
      GPIO.output(7,True)
    if Request == 'off_2':
      GPIO.output(7,False)
    if Request == 'on_3':
      GPIO.output(10,True)
    if Request == 'off_3':
      GPIO.output(10,False)
    if Request == 'on_all':
      GPIO.output(5,True)
      GPIO.output(7,True)
      GPIO.output(10,True)
    if Request == 'off_all':
      GPIO.output(5,False)
      GPIO.output(7,False)
      GPIO.output(10,False)
    if Request == 'security_off':
        GPIO.output(3,False)
        send="Security System Disabled"
    if Request == 'security_on':
        send="Security System Enabled"
        GPIO.output(5,False)
        GPIO.output(7,False)
        GPIO.output(10,False)
        while True:
            if Request == 'security_off':
                GPIO.output(3,0)
                i = 0
                break;
            i=GPIO.input(8)
            if i==0:
        #print("No intruders",i)
                GPIO.output(3,0)
                sleep(0.1)
            elif i==1:
                print("Intruder Detected")
                GPIO.output(3,1)
                now = datetime.now()
                subject='HOME SECUIRTY ALERT'
                header='To:'+toAdd+'\n'+'From:'+fromAdd+'\n'+'Subject:'+subject
                body='An Intruder Has Been Detected In Your Home at time: '+now.strftime("%m/%d/%Y, %H:%M:%S")
                print(header+'\n'+body)
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(smtpUser,smtpPass)
                print("Login Successful")
                s.sendmail(fromAdd,toAdd,header+'\n\n'+body)
                s.quit()
                #sleep(5)
                #GPIO.output(3,0)
                return
        #return        
server_address_httpd = ('192.168.31.45',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting Server')
httpd.serve_forever()
GPIO.cleanup()

