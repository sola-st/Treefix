# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
# Tests custom saveable object with checkpoint conversion enabled (forces
# Trackable-based checkpoint implementation).
saveable_compat.force_checkpoint_conversion()
self._custom_saveable_object(cycles, use_cpp_bindings=use_cpp_bindings)
