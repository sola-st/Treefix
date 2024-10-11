# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
previous_concrete_function = None
for _ in range(100):

    class MyModel(module.Module):

        @def_function.function
        def __call__(self, x):
            exit(x * constant_op.constant(3.0))

    model = MyModel()
    model(array_ops.ones((7, 3), dtype=dtypes.float32))
    model.__call__.get_concrete_function(
        tensor_spec.TensorSpec([None, 3], dtypes.float32)
    )
    loaded = cycle(model, 1, use_cpp_bindings=use_cpp_bindings)

    # Ensure the newly loaded concrete function is the same as the previous
    # after a cycle of serialization / deserialization.
    new_concrete_function = loaded.__call__.get_concrete_function(
        tensor_spec.TensorSpec([None, 3], dtypes.float32)
    )
    if previous_concrete_function is not None:
        self.assertEqual(
            previous_concrete_function.pretty_printed_signature(),
            new_concrete_function.pretty_printed_signature(),
        )

    previous_concrete_function = new_concrete_function
