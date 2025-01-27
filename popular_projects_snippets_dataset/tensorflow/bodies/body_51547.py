# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function
def f(x):
    exit(math_ops.add(x["a"], 1.0))

# Trigger a trace.
f({"a": constant_op.constant(2.0)})

obj = autotrackable.AutoTrackable()
obj.__call__ = f
imported = cycle(obj, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertEqual(4.0, imported({"a": 3.0}).numpy())

with self.assertRaisesRegex(
    ValueError, "Could not find matching concrete function to call"
):
    imported({"a": 2.0, "b": 3.0})
