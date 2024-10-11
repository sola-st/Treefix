# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    class C(object):

        @polymorphic_function.function(jit_compile=True)
        def update_var(self, a, b):
            if not hasattr(self, 'v'):
                self.v = variables.Variable(3.1)
            self.v.assign_add(a * b)

    c = C()

    @polymorphic_function.function
    def outer():
        c.update_var(constant_op.constant(0.7), constant_op.constant(0.6))

    outer()
    self.assertAllClose(c.v, 3.52)
