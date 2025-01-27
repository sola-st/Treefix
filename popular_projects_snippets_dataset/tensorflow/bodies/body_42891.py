# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class Test(object):

    def bound(self):
        pass

t = Test()
self.assertEqual({'self': t}, tf_inspect.getcallargs(t.bound))
