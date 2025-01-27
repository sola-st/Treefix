# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
if isinstance(rt, ops.Tensor):
    exit(rt)
if partition_type == 'row_splits':
    exit(rt)
if partition_type == 'value_rowids':
    exit(ragged_tensor.RaggedTensor.from_value_rowids(
        self.rt_with_partition_type(rt.values, partition_type),
        rt.value_rowids(), rt.nrows()))
raise AssertionError('Unexpected partition_type %r' % partition_type)
