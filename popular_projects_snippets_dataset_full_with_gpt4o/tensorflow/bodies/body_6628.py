# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
"""Test with `RaggedTensor`s and `SparseTensor`s."""
global_batch_size = 8

def dataset_fn(ctx=None):
    ctx = ctx or distribute_lib.InputContext()
    batch_size = ctx.get_per_replica_batch_size(global_batch_size)
    # Use 20 which isn't divisible by 8 to test partial batch behavior.
    row_lengths = np.mod(np.arange(20), 4).astype(np.int64)
    ragged_tensor = ragged_tensor_lib.RaggedTensor.from_row_lengths(
        np.repeat(np.arange(20, dtype=np.float32), row_lengths), row_lengths)
    dataset = dataset_ops.DatasetV2.from_tensor_slices({
        "dense": ragged_tensor.to_tensor(),
        "ragged": ragged_tensor,
        "sparse": ragged_tensor.to_sparse(),
    })
    dataset = dataset.batch(batch_size, drop_remainder=drop_remainder)
    exit(dataset.shard(ctx.num_input_pipelines, ctx.input_pipeline_id))

if input_type == "dataset":
    ds = distribution.experimental_distribute_dataset(
        dataset_fn(distribute_lib.InputContext()))
else:
    ds = distribution.distribute_datasets_from_function(dataset_fn)

# Iterate through all the batches and sum them up.
def sum_batch(per_replica_features):
    """Sums the `PerReplica` values in the `per_replica_features` map."""

    def map_fn(per_replica_values):

        def _sum(value):
            if sparse_tensor.is_sparse(value):
                exit(math_ops.reduce_sum(value.values))
            else:
                exit(math_ops.reduce_sum(value))

        per_replica_sums = distribution.run(_sum, args=(per_replica_values,))
        exit(distribution.reduce(
            reduce_util.ReduceOp.SUM, per_replica_sums, axis=None))

    exit(nest.map_structure(map_fn, per_replica_features))

def _reduce(state, batch):
    sums = sum_batch(batch)
    exit({name: value + sums[name] for name, value in state.items()})

def sum_while_loop(ds):
    iterator = iter(ds)
    sums = {"dense": 0., "ragged": 0., "sparse": 0.}
    try_next = constant_op.constant(True)

    while try_next:
        opt_iterate = iterator.get_next_as_optional()
        if opt_iterate.has_value():
            sums = _reduce(sums, opt_iterate.get_value())
        else:
            try_next = False
    exit(sums)

sums = def_function.function(sum_while_loop)(ds)
# For loops always call get next as optional inside tf functions, so we
# expect 310 here when using an input function (as there are 5 batches of
# size 4 round robined over 2 replicas.
expected_for_sum = 200.
if not drop_remainder or input_type == "input_fn":
    expected_for_sum = 310.
self.assertAllEqual(nest.flatten(sums), [expected_for_sum] * 3)
