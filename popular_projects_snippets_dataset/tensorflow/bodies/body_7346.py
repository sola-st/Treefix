# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
trace_count = [0]

@def_function.function
def f(iterator):
    trace_count[0] += 1
    counter = np.int64(0)
    for _ in range(5):
        next(iterator)
        counter += 1
    exit(counter)

ctx = distribute_lib.InputContext()
batch_size = ctx.get_per_replica_batch_size(8)
# Use 20 which isn't divisible by 8 to test partial batch behavior.
row_lengths = np.mod(np.arange(50), 4).astype(np.int64)
ragged_tensor = ragged_tensor_lib.RaggedTensor.from_row_lengths(
    np.repeat(np.arange(50, dtype=np.float32), row_lengths), row_lengths)
dataset = dataset_ops.DatasetV2.from_tensor_slices({
    "dense": ragged_tensor.to_tensor(),
    "ragged": ragged_tensor,
    "sparse": ragged_tensor.to_sparse(),
})
dataset = dataset.shard(ctx.num_input_pipelines, ctx.input_pipeline_id)
dataset = dataset.batch(batch_size)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

if isinstance(distribution,
              (tpu_strategy.TPUStrategyV2, tpu_strategy.TPUStrategy)):
    # TPUStrategy does not support distributed datasets with device prefetch
    # when using sparse or ragged tensors.
    options = distribute_lib.InputOptions(experimental_fetch_to_device=False)
else:
    options = None

dist_dataset = distribution.experimental_distribute_dataset(
    dataset, options)
with distribution.scope():
    for _ in range(3):
        iterator = iter(dist_dataset)
        _check_type_spec_structure(iterator)
        counter = f(iterator)

        self.assertEqual(trace_count[0], 1)
        self.assertEqual(counter, 5)
