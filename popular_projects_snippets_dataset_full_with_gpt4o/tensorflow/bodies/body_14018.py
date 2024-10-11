# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
a = dict(x=1, y=[1, 2])
b = dict(x=2, y=[3, 4])
c = dict(x=3, y=[5, 6])
d = dict(x=4, y=[7, 8])
st1 = StructuredTensor.from_pyval([a, b, c, d])

st2 = st1.partition_outer_dimension(
    row_partition.RowPartition.from_row_splits([0, 2, 2, 3, 4]))
self.assertAllEqual(st2, [[a, b], [], [c], [d]])

st3 = st2.partition_outer_dimension(
    row_partition.RowPartition.from_row_lengths([1, 0, 3, 0]))
self.assertAllEqual(st3, [[[a, b]], [], [[], [c], [d]], []])

# If we partition with uniform_row_lengths, then `x` is partitioned into
# a Tensor (not a RaggedTensor).
st4 = st1.partition_outer_dimension(
    row_partition.RowPartition.from_uniform_row_length(
        uniform_row_length=2, nvals=4, nrows=2))
self.assertAllEqual(
    st4,
    structured_tensor.StructuredTensor.from_pyval(
        [[a, b], [c, d]],
        structured_tensor.StructuredTensor.Spec(
            _ragged_shape=DynamicRaggedShape.Spec(
                row_partitions=[],
                static_inner_shape=[2, 2],
                dtype=dtypes.int64),
            _fields={
                "x":
                    tensor_spec.TensorSpec([2, 2], dtypes.int32),
                "y":
                    ragged_tensor.RaggedTensorSpec([2, 2, None],
                                                   dtypes.int32)
            })))
