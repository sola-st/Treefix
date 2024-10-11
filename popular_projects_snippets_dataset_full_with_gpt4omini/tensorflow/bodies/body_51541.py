# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def full_function(a, b, c=3.0):
    exit((a, b, c))

partial = functools.partial(full_function, 1, c=4)
self.assertAllEqual((1, 2.0, 4), partial(2.0))

signature = [tensor_spec.TensorSpec([], dtypes.float32)]
func = def_function.function(partial, input_signature=signature)

root = autotrackable.AutoTrackable()
root.f = func
a, b, c = root.f(2.0)
self.assertAllEqual([a.numpy(), b.numpy(), c.numpy()], (1, 2.0, 4))

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
a, b, c = root.f(3.0)
self.assertAllEqual([a.numpy(), b.numpy(), c.numpy()], (1, 3.0, 4))
