import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.

GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 12 to output mode.
<<<<<<< HEAD
pwm = GPIO.PWM(18, 50)   # Initialize PWM on pwmPin 100Hz frequency
=======
pwm = GPIO.PWM(12, 50)   # Initialize PWM on pwmPin 100Hz frequency
>>>>>>> db7c43e59ac02cb94c2d55242cc482e755c2d4f5
GPIO.setup(16,GPIO.OUT)
pwm2 = GPIO.PWM(16,50)

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle
pwm2.start(dc)
try:
  while True:                      # Loop until Ctl C is pressed to stop.
    for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
      pwm.ChangeDutyCycle(dc)
      pwm2.ChangeDutyCycle(dc)
      time.sleep(0.05)             # wait .05 seconds at current LED brightness
      print(dc)
    for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
      pwm.ChangeDutyCycle(dc)
      pwm2.ChangeDutyCycle(dc)
      time.sleep(0.05)             # wait .05 seconds at current LED brightness
      print(dc)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
