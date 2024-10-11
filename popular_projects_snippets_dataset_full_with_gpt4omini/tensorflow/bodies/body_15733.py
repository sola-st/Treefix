# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
"""Tests ragged_concat with a single tensor input.

    Usually, we pass a list of values in for rt_inputs.  However, you can
    also pass in a single value (as with tf.concat), in which case it simply
    returns that tensor.  This test exercises that path.
    """
rt_inputs = ragged_factory_ops.constant([[1, 2], [3, 4]])
concatenated = ragged_concat_ops.concat(rt_inputs, 0)
self.assertAllEqual(concatenated, [[1, 2], [3, 4]])
