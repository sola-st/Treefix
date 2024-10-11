# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
root.dep_one = autotrackable.AutoTrackable()
root.dep_two = autotrackable.AutoTrackable()
root.dep_two.dep = autotrackable.AutoTrackable()
root.dep_three = root.dep_two.dep
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertIs(imported.dep_three, imported.dep_two.dep)
self.assertIsNot(imported.dep_one, imported.dep_two)
