def simple_coroutine():
    print('starting ')
    x = yield
    print('do something {}'.format(x))

task = simple_coroutine()
print(task)
print(next(task))
print(task.send("hello"))