# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
self.assertEqual(np.float32,
                 type(float_type(3.5) + np.array(2.25, np.float32)))
self.assertEqual(np.float32,
                 type(np.array(3.5, np.float32) + float_type(2.25)))
