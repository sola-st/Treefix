# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
self.assertTrue(inspect_utils.isbuiltin(enumerate))
self.assertTrue(inspect_utils.isbuiltin(eval))
self.assertTrue(inspect_utils.isbuiltin(float))
self.assertTrue(inspect_utils.isbuiltin(int))
self.assertTrue(inspect_utils.isbuiltin(len))
self.assertTrue(inspect_utils.isbuiltin(range))
self.assertTrue(inspect_utils.isbuiltin(zip))
self.assertFalse(inspect_utils.isbuiltin(function_decorator))
