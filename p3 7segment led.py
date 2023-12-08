
from time import sleep
import tm1637
try:
    import thread
except ImportError:
    import _thread as thread

Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)
try:
    print ("Starting clock in the background (press CTRL + C to stop):")
    Display.StartClock(military_time=True)
    Display.SetBrightness(1.0)
    while True:
        Display.ShowDoublepoint(True)
        sleep(1)
        Display.ShowDoublepoint(False)
        sleep(1)
    Display.StopClock()
    thread.interrupt_main()
except KeyboardInterrupt:
    print ("Properly closing the clock and open GPIO pins")
    Display.cleanup()
