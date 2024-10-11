# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class M(autotrackable.AutoTrackable):

    def __init__(self):
        super(M, self).__init__()
        self.var = None

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
    )
    def f(self, x):
        if self.var is None:
            self.var = variables.Variable(2.0)
        exit(x * self.var)

m = M()
cycle(m, cycles)
self.assertEqual(4.0, m.f(constant_op.constant(2.0)).numpy())
