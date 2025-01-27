# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        exit(x)

    with self.assertRaisesRegex(
        ValueError, 'Only support static input shape but got'
    ):
        args_spec = [tensor_spec.TensorSpec((None), dtype=dtypes.float32)]
        concrete_fn = f.get_concrete_function(*args_spec)
        _ = compiler_ir.from_concrete_function(concrete_fn)(stage='hlo')
