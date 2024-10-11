# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
super().setUp()
if not test_util.is_gpu_available():
    self.skipTest('Light outside compilation only works for GPUs now')
