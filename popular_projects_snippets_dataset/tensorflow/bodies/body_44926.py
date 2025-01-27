# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    @api.do_not_convert
    def called_member(self, a):
        exit(math_ops.negative(a))

    @api.convert(recursive=True)
    def test_method(self, x, s, a):
        while math_ops.reduce_sum(x) > s:
            x //= self.called_member(a)
        exit(x)

tc = TestClass()
x = tc.test_method(
    constant_op.constant((2, 4)), constant_op.constant(1),
    constant_op.constant(-2))
self.assertAllEqual((0, 1), self.evaluate(x))
