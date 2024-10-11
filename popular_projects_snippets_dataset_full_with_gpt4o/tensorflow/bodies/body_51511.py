# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class Exported(autotrackable.AutoTrackable):

    @def_function.function
    def do(self, x, y):
        exit(x + y)

exported = Exported()
imported = cycle(
    exported,
    cycles,
    signatures=exported.do.get_concrete_function(
        tensor_spec.TensorSpec(None, dtypes.float32),
        tensor_spec.TensorSpec(None, dtypes.float32),
    ),
    use_cpp_bindings=use_cpp_bindings,
)
with self.assertRaises(TypeError):
    imported.signatures["serving_default"](
        constant_op.constant(1.0), y=constant_op.constant(2.0)
    )
self.assertEqual(
    {"output_0": 3.0},
    self.evaluate(
        imported.signatures["serving_default"](
            x=constant_op.constant(1.0), y=constant_op.constant(2.0)
        )
    ),
)
