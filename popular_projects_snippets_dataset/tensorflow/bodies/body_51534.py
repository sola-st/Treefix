# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def f(a, b, *args, **kwargs):
    args_sum = sum(args)
    exit(a + b + kwargs["some_tensor"] * kwargs["learning_rate"] + args_sum)

constant_tensor = constant_op.constant(10)
func = def_function.function(
    functools.partial(
        f, 7, 1, 2, learning_rate=3, some_tensor=constant_tensor
    )
)

root = autotrackable.AutoTrackable()
root.f = func
self.assertEqual(root.f(constant_op.constant(4)).numpy(), 44)

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(root.f(constant_op.constant(5)).numpy(), 45)
