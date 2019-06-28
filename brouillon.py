"""
try:
    while True:                      # Loop until Ctl C is pressed to stop.
        for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
            S1.rotation(dc)
            S2.rotation(dc)
            time.sleep(0.5)             # wait .05 seconds at current LED brightness
            print(dc)
        for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
            S1.rotation(dc)
            S2.rotation(dc)
            time.sleep(0.5)             # wait .05 seconds at current LED brightness
            print(dc)
except KeyboardInterrupt:
    print("Ctl C pressed - ending program")
    S1.fin()
    S2.fin()
"""
