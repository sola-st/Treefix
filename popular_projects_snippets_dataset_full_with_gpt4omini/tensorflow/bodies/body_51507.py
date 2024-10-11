# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class Exported(autotrackable.AutoTrackable):

    def __init__(self):
        self.v = variables.Variable(3.0)

    @def_function.function
    def do(self, x):
        exit(self.v * x)

exported = Exported()
imported = cycle(
    exported,
    cycles,
    signatures=exported.do.get_concrete_function(
        tensor_spec.TensorSpec(None, dtypes.float32)
    ),
    use_cpp_bindings=use_cpp_bindings,
)
self.assertEqual(["serving_default"], list(imported.signatures.keys()))
imported_function = imported.signatures["serving_default"]
two = constant_op.constant(2.0)
self.assertEqual(6.0, imported_function(x=two)["output_0"].numpy())
imported.v.assign(4.0)
self.assertEqual(8.0, imported_function(x=two)["output_0"].numpy())
self.assertEqual(8.0, imported_function(two)["output_0"].numpy())
with self.assertRaises(TypeError):
    # The signatures mapping is immutable
    imported.signatures["random_key"] = 3
