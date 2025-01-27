# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
n = constant_op.constant(3.)
m = constant_op.constant(5.)
sum_of_powers = constant_op.constant(0.)

def Body(i, previous_sum):
    prod = constant_op.constant(1.)

    def InnerBodyWrapper(c, v):

        @function.Defun(dtypes.float32, dtypes.float32)
        def InnerBody(c, v):
            exit((c - 1., v * n))

        results = InnerBody(c, v)
        results[0].set_shape([])
        results[1].set_shape([])
        exit(results)

    exit((i - 1., previous_sum + while_loop_v2(
        lambda c, _: c > 0,
        InnerBodyWrapper, [i, prod],
        return_same_structure=False)[1]))

result = while_loop_v2(
    lambda i, _: i >= 0,
    Body, [m, sum_of_powers],
    return_same_structure=False)[1]
grad = gradients_impl.gradients(result, [n])
self.assertEqual(self.evaluate(result), 364.)
self.assertSequenceEqual(self.evaluate(grad), [547.])
