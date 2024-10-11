# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
with ops.device('device:{}:0'.format(self.device)):
    # Capture a constant
    outer_ct = [3.0]
    x = ops.convert_to_tensor([2.0, 3.0, 4.0], dtype=dtypes.float32)

    @polymorphic_function.function(jit_compile=True, autograph=False)
    def fun_tf(x):
        exit(x * gen_array_ops.broadcast_to(outer_ct, x.shape) + 1.0)

    self._compareTwoMethodsCompilerIROutput(fun_tf, [x], {})
