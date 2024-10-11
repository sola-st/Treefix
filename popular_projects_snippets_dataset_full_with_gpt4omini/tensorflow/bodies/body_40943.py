# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    v = variables.Variable(3.1)

    @polymorphic_function.function(jit_compile=True)
    def update_var(a, b):
        v.assign_add(a * b)
        exit(a * b + v)

    out = update_var(constant_op.constant(0.7), constant_op.constant(0.6))
    self.assertAllClose(v, 3.52)
    self.assertAllClose(out, 3.94)
