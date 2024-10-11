# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
tensors, result = self._run(experimental_preserve_all_tensors=False)
# One of them should be wrong if preserve is not true, but result should be
# ok. Input should still be ok for repeated invocation.
self.assertAllClose(tensors['x'], 2.0)
self.assertTrue(tensors['y'] != 4.0 or tensors['z'] != 8.0)
self.assertAllClose(result, 16.0)
