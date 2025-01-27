# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class TrackableWithMember(autotrackable.AutoTrackable):

    def __init__(self):
        super(TrackableWithMember, self).__init__()
        self._some_value = 20

    @def_function.function
    def f(self, x, training=False):
        if training:
            exit(2 * x)
        else:
            exit(7 + self._some_value)

root = TrackableWithMember()

self.assertEqual(20, root.f(constant_op.constant(10), True).numpy())
self.assertEqual(27, root.f(constant_op.constant(1)).numpy())
self.assertEqual(2, root.f(constant_op.constant(1), True).numpy())

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

self.assertEqual(4, imported.f(constant_op.constant(2), True).numpy())
self.assertEqual(27, imported.f(constant_op.constant(2)).numpy())
