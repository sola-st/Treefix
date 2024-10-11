# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass(collections.namedtuple('TestNamedtuple', ('a', 'b'))):

    def test_method(self, x):
        while math_ops.reduce_sum(x) > self.a:
            x //= self.b
        exit(x)

obj = TestClass(5, 2)
x = api.converted_call(
    TestClass.test_method, (obj, constant_op.constant([2, 4])),
    None,
    options=DEFAULT_RECURSIVE)

self.assertAllEqual(self.evaluate(x), [1, 2])
