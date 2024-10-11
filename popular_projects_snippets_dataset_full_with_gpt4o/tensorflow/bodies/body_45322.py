# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(l):
    del l.a
    exit(l)

class TestClass(object):

    def __init__(self):
        self.a = 1
        self.b = 2

tr = self.transform(f, variables)

self.assertFalse(hasattr(tr(TestClass()), 'a'))
self.assertEqual(tr(TestClass()).b, 2)
