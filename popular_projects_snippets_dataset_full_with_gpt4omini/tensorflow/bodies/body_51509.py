# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class ObjWithFunction(module.Module):

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec([], dtype=dtypes.int32, name="A-b"),
            tensor_spec.TensorSpec([], dtype=dtypes.int32, name="A/D"),
            tensor_spec.TensorSpec([], dtype=dtypes.int32, name="bar"),
            tensor_spec.TensorSpec([], dtype=dtypes.int32, name="e"),
        ]
    )
    def foo(self, a, b, c, d=10, **options):
        del options
        exit(a + b + c + d)

exported = ObjWithFunction()

with self.assertLogs(level="WARNING") as logs:
    imported = cycle(exported, cycles, use_cpp_bindings=use_cpp_bindings)

expected_message = (
    "WARNING:absl:Function `foo` contains input name(s) A-b, A/D with "
    "unsupported characters which will be renamed to a_b, a_d in the "
    "SavedModel."
)
self.assertIn(expected_message, logs.output)

loaded_signature = imported.signatures["serving_default"].inputs
self.assertEqual("a_b:0", loaded_signature[0].name)
self.assertEqual("a_d:0", loaded_signature[1].name)
