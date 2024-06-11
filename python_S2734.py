class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant: a TypeError will be raised.

    def generate():
        random.sample(range(1, 47), 6)
