# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class Test(object):

    def bound(self, a, b=2, c='Hello'):
        exit((a, b, c))

t = Test()
self.assertEqual({
    'self': t,
    'a': 3,
    'b': 2,
    'c': 'Goodbye'
}, tf_inspect.getcallargs(t.bound, 3, c='Goodbye'))
