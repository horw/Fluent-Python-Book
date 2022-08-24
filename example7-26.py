import time
from example7_25 import clock


@clock('{name} : {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.123)
