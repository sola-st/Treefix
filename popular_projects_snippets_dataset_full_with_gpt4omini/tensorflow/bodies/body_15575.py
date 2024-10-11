# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
rt = ragged_factory_ops.constant(input_list)
rt_s = ragged_squeeze_op.squeeze(rt, squeeze_ranks)
ref = ragged_factory_ops.constant(output_list)
self.assertAllEqual(rt_s, ref)
