import schedule
import time

def func():
    print('vishwaGW')

schedule.every(1).minute.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)

