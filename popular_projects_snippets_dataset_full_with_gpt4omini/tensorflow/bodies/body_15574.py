# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
dt = constant_op.constant(input_list)
rt = ragged_conversion_ops.from_tensor(dt)
rt_s = ragged_squeeze_op.squeeze(rt, squeeze_ranks)
dt_s = array_ops.squeeze(dt, squeeze_ranks)
self.assertAllEqual(ragged_conversion_ops.to_tensor(rt_s), dt_s)
