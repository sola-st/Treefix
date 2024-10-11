# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py

with ops.device('device:{}:0'.format(self.device)):

    class C(object):

        @polymorphic_function.function(jit_compile=True)
        def f1(self, x, a):
            exit(x + a)

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    c = C()
    self.assertAllClose([2, 3, 3, 4, 4], c.f1(inputs, 1))
