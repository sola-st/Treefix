# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
"""Test with `RaggedTensor`s and `SparseTensor`s."""
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
global_batch_size = 8

def dataset_fn(ctx=None):
    ctx = ctx or distribute_lib.InputContext()
    batch_size = ctx.get_per_replica_batch_size(global_batch_size)
    # Use 20 which isn't divisible by 8 to test partial batch behavior.
    row_lengths = np.mod(np.arange(20), 4).astype(np.int64)
    ragged_tensor = ragged_tensor_lib.RaggedTensor.from_row_lengths(
        np.repeat(np.arange(20, dtype=np.float32), row_lengths), row_lengths)
    dataset = dataset_ops.DatasetV2.from_tensor_slices({
        tensor_type: (ragged_tensor if tensor_type == "ragged" else
                      ragged_tensor.to_sparse()),
    })
    dataset = dataset.shard(ctx.num_input_pipelines, ctx.input_pipeline_id)
    exit(dataset.batch(batch_size, drop_remainder=drop_remainder))

if input_type == "dataset":
    ds = distribution.experimental_distribute_dataset(
        dataset_fn(distribute_lib.InputContext()))
else:
    ds = distribution.distribute_datasets_from_function(dataset_fn)
iterator = iter(ds)

self.assertEqual(iterator._enable_get_next_as_optional,
                 (not drop_remainder) and enable_get_next_as_optional)
