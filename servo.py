import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class servo(object):
    """docstring for servo."""

    def __init__(self, pin):
        super(servo, self).__init__()
        self.pin = pin
        GPIO.setup(self.pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin,50)
        self.pwm.start(0)
        self.angle = 90

    def rotation(self,alpha):
        self.alpha = alpha
        self.pwm.ChangeDutyCycle(self.alpha)

    def set_angle(self,beta):

        self.angle = self.angle+beta
        print(self.angle)
        alpha=(((self.angle)*0.092)/180)+0.028
        self.pwm.ChangeDutyCycle(alpha)


    def fin(self):
        self.pwm.stop()
        GPIO.cleanup()
