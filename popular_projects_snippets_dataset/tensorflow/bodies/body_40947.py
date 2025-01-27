# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('TPU generates different HLO')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(a, b):
        exit(array_ops.transpose(a, b))

    a = array_ops.ones([3, 4, 3], dtype=dtypes.float32)
    b = constant_op.constant([0, 2, 1], dtype=dtypes.int32)

    self.assertIn('{2,1,0}',
                  f.experimental_get_compiler_ir(a, b)(stage='optimized_hlo'))
