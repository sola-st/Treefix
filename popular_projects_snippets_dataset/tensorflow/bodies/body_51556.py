# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = checkpoint.Checkpoint()
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(versions.__version__, root.tensorflow_version)
self.assertEqual(versions.__git_version__, root.tensorflow_git_version)
