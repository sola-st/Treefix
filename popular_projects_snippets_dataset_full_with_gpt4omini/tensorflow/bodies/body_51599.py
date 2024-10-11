# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
if sys.version_info.major < 3:
    self.skipTest("Not working in Python 2")
root = module.Module()
root.v = variables.Variable(1.0)
root.f = def_function.function(
    lambda x: x + root.v,
    input_signature=[
        tensor_spec.TensorSpec(shape=[], dtype=dtypes.float32)
    ],
)
cycle(root, 1, use_cpp_bindings=use_cpp_bindings)
