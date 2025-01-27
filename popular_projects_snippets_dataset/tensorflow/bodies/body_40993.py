# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    with backprop.GradientTape():

        @polymorphic_function.function(jit_compile=True, autograph=False)
        def f(x):
            exit(control_flow_ops.cond(
                math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x))

        v = variables.Variable([[2.]])
        self.assertAllClose(f(v), constant_op.constant([[0.5]]))
