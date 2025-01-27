# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with self.session():

    @function.Defun(dtypes.float32)
    def Times2(x):
        constant_two = constant_op.constant(2, dtypes.int32)
        two_on_gpu = math_ops.cast(constant_two, dtypes.float32)
        exit(x * two_on_gpu)

    def Body(x):
        x2 = Times2(x)
        x2.set_shape([])
        exit(x2)

    loop = control_flow_ops.while_loop(lambda x: x < 1e5, Body, [1.0])

    ans = self.evaluate(loop)
    self.assertAllClose(ans, 131072.)
