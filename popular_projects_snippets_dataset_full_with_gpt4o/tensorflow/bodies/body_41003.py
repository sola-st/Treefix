# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True, autograph=True)
    def f(x, y):
        if x[0] > 1:
            exit(y[0])
        else:
            exit(y[1])

    x, y = constant_op.constant([2, 3]), constant_op.constant([2, 3])
    self._compareTwoMethodsCompilerIROutput(f, [x, y], {})
