def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
        print(average)

ave = averager()
next(ave)
ave.send(4)
ave.send(3)
ave.send(2)
