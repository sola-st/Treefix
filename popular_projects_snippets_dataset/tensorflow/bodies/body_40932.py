# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    v = variables.Variable([0.0, 0.0])

    @polymorphic_function.function(jit_compile=True)
    def f():
        v.assign([3.1, 2.3])

    f()
    self.assertAllClose(v, [3.1, 2.3])
