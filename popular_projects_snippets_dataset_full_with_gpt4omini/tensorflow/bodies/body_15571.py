# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_stack_op_test.py
"""Tests ragged_stack with a single tensor input.

    Usually, we pass a list of values in for rt_inputs.  However, you can
    also pass in a single value (as with tf.stack), in which case it is
    equivalent to expand_dims(axis=0).  This test exercises that path.
    """
rt_inputs = ragged_factory_ops.constant([[1, 2], [3, 4]])
stacked = ragged_concat_ops.stack(rt_inputs, 0)
self.assertAllEqual(stacked, [[[1, 2], [3, 4]]])
