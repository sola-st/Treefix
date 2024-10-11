# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
self.assertEqual(float_type(1.2), float_type("1.2"))
self.assertTrue(np.isnan(float_type("nan")))
self.assertTrue(np.isnan(float_type("-nan")))
if dtype_has_inf(float_type):
    self.assertEqual(float_type(float("inf")), float_type("inf"))
    self.assertEqual(float_type(float("-inf")), float_type("-inf"))
