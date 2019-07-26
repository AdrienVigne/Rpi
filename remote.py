#!/usr/bin/python3
import asyncio

import io
import picamera
import logging
import socketserver
from threading import Condition, Thread



PAGE="""\
<html>
<head>
<title>ROAMER2 streaming</title>
</head>
<body>
<h1>ROAMER2 Streaming</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""
class Thread_remote(Thread):
    """docstring for Thread_remote."""


    def __init__(self):
        super(Thread_remote, self).__init__()

    def run(self):
        from http import server
        class StreamingOutput(object):
            def __init__(self):
                self.frame = None
                self.buffer = io.BytesIO()
                self.condition = Condition()

            def write(self, buf):
                if buf.startswith(b'\xff\xd8'):
                    # New frame, copy the existing buffer's content and notify all
                    # clients it's available
                    self.buffer.truncate()
                    with self.condition:
                        self.frame = self.buffer.getvalue()
                        self.condition.notify_all()
                    self.buffer.seek(0)
                return self.buffer.write(buf)

        class StreamingHandler(server.BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(301)
                    self.send_header('Location', '/index.html')
                    self.end_headers()
                elif self.path == '/index.html':
                    content = PAGE.encode('utf-8')
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')
                    self.send_header('Content-Length', len(content))
                    self.end_headers()
                    self.wfile.write(content)
                elif self.path == '/stream.mjpg':
                    self.send_response(200)
                    self.send_header('Age', 0)
                    self.send_header('Cache-Control', 'no-cache, private')
                    self.send_header('Pragma', 'no-cache')
                    self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
                    self.end_headers()
                    try:
                        while True:
                            with output.condition:
                                output.condition.wait()
                                frame = output.frame
                            self.wfile.write(b'--FRAME\r\n')
                            self.send_header('Content-Type', 'image/jpeg')
                            self.send_header('Content-Length', len(frame))
                            self.end_headers()
                            self.wfile.write(frame)
                            self.wfile.write(b'\r\n')
                    except Exception as e:
                        logging.warning(
                            'Removed streaming client %s: %s',
                            self.client_address, str(e))
                else:
                    self.send_error(404)
                    self.end_headers()

        class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
            allow_reuse_address = True
            daemon_threads = True


        print("remote")
        with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
            output = StreamingOutput()
            camera.start_recording(output, format='mjpeg')
            try:
                address = ('', 8000)
                server = StreamingServer(address, StreamingHandler)
                server.serve_forever()
            finally:
                camera.stop_recording()



import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)




class Thread_serveur(Thread):
    """docstring for Thread_serveur."""

    time.sleep(10)

    def __init__(self):
        super(Thread_serveur, self).__init__()

    def Allumer(self):
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(23,GPIO.HIGH)

    def Eteindre(self):
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)

    def run(self):
        from servo import *
        import socket

        S1 = servo(12)
        S2 = servo(16)

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try :
            sock.bind(("192.168.1.62",35351))
        except :
            sock.close()
            sock.bind(("192.168.1.62",35351))
        print("Serveur d'écoute sur le port : ",35351)
        sock.listen(5)
        print("attente connexion")
        connexion,adresse=sock.accept()
        print("client conneté ip : %s, port : %s",adresse[0],adresse[1])
        while 1 :
            msg = connexion.recv(1024)
            msg = msg.decode()
            if msg == 'q':
                connexion.close()
                sock.close()
                break
            if msg == 'up':
                S1.set_angle(1)
            if msg == 'down':
                S1.set_angle(-1)
            if msg == 'right':
                S2.set_angle(1)
            if msg == 'left':
                S2.set_angle(-1)





t1 = Thread_remote()
t2 = Thread_serveur()

t1.start()
t2.start()
