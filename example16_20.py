import collections

Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """Yield to simulator"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident,'going home')


taxi = taxi_process(ident=13, trips=2, start_time=0)
event = next(taxi)
while True:
    event = taxi.send(event.time+1)
    print(event)