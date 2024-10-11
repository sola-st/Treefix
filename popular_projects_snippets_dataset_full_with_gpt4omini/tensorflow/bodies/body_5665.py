# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
class Foo(object):

    def __init__(self, x):
        self.x = x

v = values_lib.DistributedDelegate((Foo(7), Foo(8)))
self.assertEqual(7, v.x)
with self.assertRaises(AttributeError):
    _ = v.y
