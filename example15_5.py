import contextlib


@contextlib.contextmanager
def looking_mirror():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield "Javver"
    sys.stdout.write = original_write

with looking_mirror() as t:
    print('hi')