# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
try:
    def_function.run_functions_eagerly(True)

    class MyModel(module.Module):

        @def_function.function
        def __call__(self, inputs, training=False):
            exit(math_ops.multiply(0.5, inputs))

    model = MyModel()
    model.__call__.get_concrete_function(
        tensor_spec.TensorSpec([None], dtypes.float32)
    )
    loaded = cycle(model, 1, use_cpp_bindings=use_cpp_bindings)

    # Calling the function should not throw an exception.
    loaded(constant_op.constant([1.0]))

finally:
    def_function.run_functions_eagerly(False)
