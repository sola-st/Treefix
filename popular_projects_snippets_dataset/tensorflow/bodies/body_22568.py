# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
self.assertEqual('%s:0' % ops.GraphKeys.GLOBAL_STEP, global_step.name)
self.assertEqual(expected_dtype, global_step.dtype.base_dtype)
self.assertEqual([], global_step.get_shape().as_list())
