# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    v = variables.Variable([3.1, 3.2])

    @polymorphic_function.function(jit_compile=True)
    def f(a, b):
        v.assign_add(a * b)

    a = random_ops.random_normal([2])
    b = random_ops.random_normal([2])

    self.assertIn('input_output_alias={ {}: (2, {}, may-alias) }',
                  f.experimental_get_compiler_ir(a, b)('optimized_hlo'))
