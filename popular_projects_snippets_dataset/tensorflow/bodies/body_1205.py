# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cast_ops_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x):
        t = array_ops.bitcast(x, dtypes.float32)
        exit(math_ops.reduce_sum(t, axis=1))

    compiled_f = def_function.function(f, jit_compile=True)

    x = random_ops.random_normal([10, 10, 2], dtype=dtypes.float16)
    with ops.device(self.device):
        out = f(x)
        compiled_out = compiled_f(x)
        self.assertAllClose(out, compiled_out)
        # 10,10,2--(bitcast-convert)-->10,10--(reduce)-->10
        self.assertEqual(out.shape[0], 10)

    hlo = compiled_f.experimental_get_compiler_ir(x)(stage='hlo')
    self.assertIn('f32[10,10]{1,0} bitcast-convert(f16[10,10,2]{2,1,0}', hlo)
