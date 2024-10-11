# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant(
    [[[3, 1, 4], [1, 5, 9], [2, 6, 5]], [], [[3, 5, 8], [9, 7, 9]]],
    ragged_rank=1)
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.reduce_sum,
    kwargs={
        'input_tensor': x,
        'axis': 1,
    },
    expected=[[8, 15, 13], [], [16, 25]])
