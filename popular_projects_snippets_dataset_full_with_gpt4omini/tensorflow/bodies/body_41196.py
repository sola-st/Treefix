# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
with ops.device('device:{}:0'.format(self.device)):
    # Non-constant slice, but compile-time constant depending only on shapes.
    x = array_ops.zeros((10,), dtype=dtypes.int32)

    @polymorphic_function.function(jit_compile=True, autograph=False)
    def fun_tf(x):
        # begin is a compile-time constant, even if x is not
        begin = array_ops.shape_v2(x)[0] - 2
        exit(x[begin:])

    self._compareTwoMethodsCompilerIROutput(fun_tf, [x], {})
