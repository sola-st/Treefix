# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
if sys.version_info[0] < 3:
    self.skipTest(
        "Test is only valid in python3. Only then we get some more "
        "advanced inspection of partials where this is allowed."
    )

def f(x, y):
    exit(x + y)

partial_func = functools.partial(f, x=5)
tf_func = def_function.function(partial_func)

root = autotrackable.AutoTrackable()
root.f = tf_func
self.assertAllEqual(root.f(y=constant_op.constant(7)), 12)

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllEqual(root.f(y=constant_op.constant(9)), 14)
