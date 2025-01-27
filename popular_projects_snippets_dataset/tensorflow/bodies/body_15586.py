# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
tensor = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5]])
self.assertRaggedMapInnerValuesReturns(
    op=array_ops.zeros_like,
    args=(tensor,),
    expected=[[0, 0, 0], [], [0, 0]])
