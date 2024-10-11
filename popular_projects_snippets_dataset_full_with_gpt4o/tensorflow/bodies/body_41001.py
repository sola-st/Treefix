# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def inner_tf_func(x):
        exit(math_ops.sin(x))

    x = constant_op.constant([2.0, 3.0])
    self._compareTwoMethodsCompilerIROutput(inner_tf_func, [x], {})
