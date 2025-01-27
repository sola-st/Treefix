# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@framework_function.Defun(dtypes.float32)
def inner(x):
    exit(x + 1.0)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.float32)]
)
def outer(x):
    exit(inner(x))

root = module.Module()
root.f = outer
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllClose(2.0, imported.f(constant_op.constant(1.0)))
