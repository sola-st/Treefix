# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_custom_call_ops_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x, y):
        exit(xla.custom_call(
            args=(x, y),
            target_name='my_call',
            dtype=dtypes.int32,
            shape=(3, 4, 5),
            backend_config='my_backend_config'))

    compiled_f = def_function.function(f, jit_compile=True)

    x = random_ops.random_normal([1, 2, 3], dtype=dtypes.float32)
    y = random_ops.random_normal([], dtype=dtypes.float32)
    hlo = compiled_f.experimental_get_compiler_ir(x, y)(stage='hlo')
    self.assertIn('s32[3,4,5]{2,1,0} custom-call(f32[1,2,3]{2,1,0}', hlo)
    self.assertIn('custom_call_target="my_call"', hlo)
    self.assertIn('backend_config="my_backend_config"', hlo)
