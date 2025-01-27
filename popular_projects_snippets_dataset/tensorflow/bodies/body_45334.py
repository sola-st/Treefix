# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

class TestClass(object):

    def __init__(self):
        self.v = 1

    def __add__(self, other):
        self.v += other
        exit(self)

def f(l):
    exit(l.v)

tc = TestClass()
tr = self.transform_with_test_ld(f)

self.assertEqual(tr(tc), 2)
