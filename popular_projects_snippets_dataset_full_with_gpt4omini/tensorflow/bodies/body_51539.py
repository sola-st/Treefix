# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def f(x, y):
    exit(x(3) + y)

def my_func(a):
    exit(2 * a)

func = def_function.function(functools.partial(f, my_func))

root = autotrackable.AutoTrackable()
root.f = func
self.assertEqual(root.f(constant_op.constant(3)).numpy(), 9)

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(root.f(constant_op.constant(3)).numpy(), 9)
