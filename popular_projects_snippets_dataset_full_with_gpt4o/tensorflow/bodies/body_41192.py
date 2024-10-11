# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True, autograph=False)
    def fun_tf():
        exit(array_ops.zeros((10), dtype=dtypes.int32))

    self._compareTwoMethodsCompilerIROutput(fun_tf, [], {})
