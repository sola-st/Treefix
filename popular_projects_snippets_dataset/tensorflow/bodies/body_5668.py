# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py

class Foo(object):

    def __init__(self, x):
        self.x = x

v = values_lib.DistributedDelegate((Foo(7), Foo(8)))
v_shallow_copy = copy.copy(v)
self.assertEqual(v.x, v_shallow_copy.x)
v_deep_copy = copy.deepcopy(v)
self.assertEqual(v.x, v_deep_copy.x)
