# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def fn(x):
        exit(x - x)

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    for stage in ('hlo_serialized', 'optimized_hlo_serialized'):
        hlo = fn.experimental_get_compiler_ir(inputs)(
            stage=stage, device_name=f'/device:{self.device}:0')
        self.assertIsInstance(hlo, bytes)
    self._compareTwoMethodsCompilerIROutput(fn, [inputs], {})
