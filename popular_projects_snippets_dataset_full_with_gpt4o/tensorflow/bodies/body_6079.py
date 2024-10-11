# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
if context.num_gpus() < 1 and context.executing_eagerly():
    self.skipTest("A GPU is not available for this test in eager mode.")

mirrored = _make_mirrored()
v = mirrored.values[0]
self.assertEqual(v.name, mirrored.name)
self.assertEqual(v.dtype, mirrored.dtype)
self.assertEqual(v.shape, mirrored.shape)
