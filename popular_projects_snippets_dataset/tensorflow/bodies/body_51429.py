# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def func(x, training=True):
    # x is a nested structure, we care about one particular tensor.
    _, (a, b) = x
    if training:
        exit(2 * a["a"] + b)
    else:
        exit(7)

x = constant_op.constant(10)
y = constant_op.constant(11)

input1 = [6, ({"a": x}, y)]
input2 = [7, ({"a": x}, y)]  # Not compatible with input1 signature.
input3 = [6, ({"a": y}, x)]  # Compatible with input1 signature.

root = autotrackable.AutoTrackable()
root.f = def_function.function(func).get_concrete_function(input1)

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

with self.assertRaises(TypeError):
    imported.f(input2)

self.assertEqual(31, imported.f(input1).numpy())
self.assertEqual(32, imported.f(input3).numpy())
