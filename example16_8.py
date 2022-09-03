class DemoException(Exception):
    """Some excpetion"""

def demo_exc_handling():
    print('coroutine started')
    while True:
        try:
            x = yield
            if x!=1:
                raise DemoException
        except DemoException:
            print("DemoException Error")
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.!')


demo = demo_exc_handling()
next(demo)
demo.send(1)
demo.send('hello')
demo.send(1)