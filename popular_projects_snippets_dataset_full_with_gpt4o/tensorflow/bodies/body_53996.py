# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a = 7
b = (2., 3.)
c = np.ones((3, 2, 4)) * 7.
expected = {"a": a, "b": b, "c": c}
my_named_tuple = collections.namedtuple("MyNamedTuple", ["a", "b", "c"])

# Identity.
self.assertAllClose(expected, my_named_tuple(a=a, b=b, c=c))
self.assertAllClose(
    my_named_tuple(a=a, b=b, c=c), my_named_tuple(a=a, b=b, c=c))
