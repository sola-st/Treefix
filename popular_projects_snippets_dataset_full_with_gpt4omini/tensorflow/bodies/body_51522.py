# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(autograph=False)
def func(a=1, b=2, c=3, training=True):
    if training:
        exit([a, b, c, training])
    else:
        exit([c, b, a, training])

    # TODO(b/123501567): Work-around to trigger generic traces of a function
    # with extra non tensor args.
signature = 3 * [tensor_spec.TensorSpec(None, dtypes.float32)]

@def_function.function(input_signature=signature)
def trigger(a, b, c):
    func(a, b, c, True)
    func(a, b, c, False)

trigger.get_concrete_function()

root = autotrackable.AutoTrackable()
root.f = func
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllEqual(root.f(), [1.0, 2.0, 3.0, True])
self.assertAllEqual(root.f(-1.0, training=False), [3.0, 2.0, -1.0, False])

with self.assertRaisesRegex(
    ValueError, "Could not find matching concrete function"
):
    root.f(["hello", 1.0])
