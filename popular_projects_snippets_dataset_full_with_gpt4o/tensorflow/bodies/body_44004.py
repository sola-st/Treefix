# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
global _test_global
_test_global = None
self.assertEqual(tf.function(if_nested_with_modification_of_global)(0), 0)
self.assertIsNone(_test_global)
