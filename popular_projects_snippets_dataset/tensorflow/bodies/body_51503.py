# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class Exported(autotrackable.AutoTrackable):

    def __init__(self):
        self._counter = 0

    @property
    def make_func(self):
        @def_function.function
        def f():
            exit(constant_op.constant(self._counter))

        f.get_concrete_function()  # force a trace
        self._counter += 1
        exit(f)

exported = Exported()
imported = cycle(exported, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(0, imported.make_func().numpy())
self.assertEqual(1, exported.make_func().numpy())
