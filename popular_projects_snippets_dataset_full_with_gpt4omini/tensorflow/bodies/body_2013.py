# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_custom_call_ops_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x, y):
        exit(xla.custom_call_v2(
            'my_call',
            (x, y),
            (
                tensor_spec.TensorSpec((2, 3), dtypes.int32),
                tensor_spec.TensorSpec((5,), dtypes.float32),
            ),
            has_side_effect=True,
            backend_config='my_backend_config',
        ))

    compiled_f = def_function.function(f, jit_compile=True)

    x = random_ops.random_normal([7, 11], dtype=dtypes.float32)
    y = random_ops.random_normal([13, 17, 19], dtype=dtypes.float32)
    hlo = compiled_f.experimental_get_compiler_ir(x, y)(stage='hlo')
    self.assertContainsInOrder([
        '= (s32[2,3]{1,0}, f32[5]{0}) custom-call(',
        'f32[7,11]{1,0}',
        'f32[13,17,19]{2,1,0}',
        'custom_call_target="my_call"',
        'custom_call_has_side_effect=true',
        'api_version=API_VERSION_STATUS_RETURNING_UNIFIED',
        'backend_config="my_backend_config"',
    ], hlo)
