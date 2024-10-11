# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
tensors, result = self._run(experimental_preserve_all_tensors=True)
# All intermediates should be true and result be true.
self.assertAllClose(tensors['x'], 2.0)
self.assertAllClose(tensors['y'], 4.0)
self.assertAllClose(tensors['z'], 8.0)
self.assertAllClose(result, 16.0)
