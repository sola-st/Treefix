# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x, d):
        if math_ops.reduce_all(
            math_ops.greater(x, random_ops.random_normal([10, 10]))):
            exit(array_ops.reshape(x * 2, constant_op.constant([100])))
        else:
            exit(array_ops.reshape(x * 3, d))

    f(random_ops.random_normal([10, 10]), constant_op.constant([100]))
