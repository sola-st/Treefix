# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
my_named_tuple = collections.namedtuple("MyNamedTuple", ["x", "y"])
l1 = [
    my_named_tuple(x=np.array([[2.3, 2.5]]), y=np.array([[0.97, 0.96]])),
    my_named_tuple(x=np.array([[3.3, 3.5]]), y=np.array([[0.98, 0.99]]))
]
l2 = [
    ([[2.3, 2.5]], [[0.97, 0.96]]),
    ([[3.3, 3.5]], [[0.98, 0.99]]),
]
self.assertAllClose(l1, l2)
