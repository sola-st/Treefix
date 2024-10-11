# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
ctx = distribute_lib.InputContext()
batch_size = ctx.get_per_replica_batch_size(8)
# Use 20 which isn't divisible by 8 to test partial batch behavior.
row_lengths = np.mod(np.arange(20), 4).astype(np.int64)
ragged_tensor = ragged_tensor_lib.RaggedTensor.from_row_lengths(
    np.repeat(np.arange(20, dtype=np.float32), row_lengths), row_lengths)
dataset = dataset_ops.DatasetV2.from_tensor_slices({
    "dense": ragged_tensor.to_tensor(),
    "ragged": ragged_tensor,
    "sparse": ragged_tensor.to_sparse(),
})
dataset = dataset.shard(ctx.num_input_pipelines, ctx.input_pipeline_id)
dataset = dataset.batch(batch_size)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
dist_dataset = distribution.experimental_distribute_dataset(dataset)
spec = dist_dataset._type_spec
self.assertEqual(spec._input_workers, dist_dataset._input_workers)
self.assertEqual(
    spec._element_spec, {
        "sparse":
            values.PerReplicaSpec(
                sparse_tensor.SparseTensorSpec(
                    tensor_shape.TensorShape([None, 3]), dtypes.float32),
                sparse_tensor.SparseTensorSpec(
                    tensor_shape.TensorShape([None, 3]), dtypes.float32)),
        "dense":
            values.PerReplicaSpec(
                tensor_spec.TensorSpec(
                    shape=(None, 3), dtype=dtypes.float32, name=None),
                tensor_spec.TensorSpec(
                    shape=(None, 3), dtype=dtypes.float32, name=None)),
        "ragged":
            values.PerReplicaSpec(
                ragged_tensor_lib.RaggedTensorSpec(
                    tensor_shape.TensorShape([None, None]), dtypes.float32,
                    1, dtypes.int64),
                ragged_tensor_lib.RaggedTensorSpec(
                    tensor_shape.TensorShape([None, None]), dtypes.float32,
                    1, dtypes.int64))
    })
