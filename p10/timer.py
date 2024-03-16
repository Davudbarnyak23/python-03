
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)

        timer = '{:02d}:{:02d}'.format(mins, secs)
        min = t//60
        secs=t%60
        print(timer)
        time.sleep(1)
        t-= 1


    print('TIME OVER!')



t = int(input('ENTER THE TIME: '))

countdown(t)