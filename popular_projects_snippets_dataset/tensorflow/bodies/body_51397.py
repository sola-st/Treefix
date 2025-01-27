# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class MakeVariable(module.Module):

    def __init__(self):
        self.v = None

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec([None], dtypes.int64)]
    )
    def make_variable(self, initial_value):
        if self.v is None:
            self.v = variables.Variable(initial_value)

m = MakeVariable()
m.make_variable([1, 2, 3])
m = cycle(m, cycles, use_cpp_bindings=use_cpp_bindings)
m.v.assign([1, 2, 3, 4])
self.assertEqual([None], tensor_shape.as_shape(m.v.shape).as_list())
