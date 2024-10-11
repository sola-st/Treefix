# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
rt = ragged_factory_ops.constant([[1, 2], [3]])
rt_value = self.evaluate(rt)
self.assertTrue(tensor_util.is_tf_type(rt))
self.assertFalse(tensor_util.is_tf_type(rt_value))
