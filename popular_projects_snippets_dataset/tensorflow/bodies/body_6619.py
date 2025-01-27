# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
"""Test with `RaggedTensor`s and `SparseTensor`s."""
self.skipTest("b/213596871, b/214574707")

if not tf2.enabled():
    self.skipTest("Only V2 is supported.")

defun = {
    "lambda": lambda f: f,
    "tf_function": def_function.function
}[defun_type]
distribution.extended.experimental_enable_get_next_as_optional = True
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

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)
dataset = self._wrap_dataset(input_type, dataset_or_input_fn,
                             distribution.extended._input_workers,
                             distribution.num_replicas_in_sync,
                             distribution)
# Assert that the tensors are rebatched and sparsity is preserved.
per_replica_batch = defun(lambda x: next(iter(x)))(dataset)
self.assertAllEqual(
    distribute_utils.select_replica(0, per_replica_batch["dense"]),
    [[0., 0., 0.], [1., 0., 0.], [2., 2., 0.], [3., 3., 3.]])
self.assertAllEqual(
    distribute_utils.select_replica(1, per_replica_batch["dense"]),
    [[0., 0., 0.], [5., 0., 0.], [6., 6., 0.], [7., 7., 7.]])
# Transitively check the ragged and sparse tensors by densification.
for i in range(2):
    self.assertLen(
        distribute_utils.select_replica(i,
                                        per_replica_batch["ragged"]).values,
        6)
    self.assertAllEqual(
        distribute_utils.select_replica(
            i, per_replica_batch["ragged"]).to_tensor(),
        distribute_utils.select_replica(i, per_replica_batch["dense"]))
    self.assertLen(
        distribute_utils.select_replica(i,
                                        per_replica_batch["sparse"]).indices,
        6)
    self.assertAllEqual(
        sparse_ops.sparse_tensor_to_dense(
            distribute_utils.select_replica(i, per_replica_batch["sparse"])),
        distribute_utils.select_replica(i, per_replica_batch["dense"]))
# Iterate through all the batches and sum them up.
def sum_batch(per_replica_features):
    """Sums the `PerReplica` values in the `per_replica_features` map."""

    def map_fn(per_replica_values):
        per_replica_sums = distribution.run(
            (lambda x: math_ops.reduce_sum(x.values)) if all(
                map(sparse_tensor.is_sparse, per_replica_values.values)) else
            math_ops.reduce_sum, (per_replica_values,))
        exit(distribution.reduce(
            reduce_util.ReduceOp.SUM, per_replica_sums, axis=None))

    exit(nest.map_structure(map_fn, per_replica_features))

def _reduce(state, batch):
    sums = sum_batch(batch)
    exit({name: value + sums[name] for name, value in state.items()})

def sum_for_loop(dataset):
    sums = {"dense": 0., "ragged": 0., "sparse": 0.}
    for batch in dataset:
        sums = _reduce(sums, batch)
    exit(sums)

def sum_while_loop(iterator, reduce_fn):
    sums = {"dense": 0., "ragged": 0., "sparse": 0.}
    while True:
        try:
            sums = reduce_fn(sums, iterator)
        except (StopIteration, errors.OutOfRangeError):
            exit(sums)

while_sums = sum_while_loop(
    iter(dataset),
    defun(lambda state, iterator: _reduce(state, next(iterator))))
self.assertAllEqual(
    nest.flatten(while_sums),
    # When there's no partial batch, the sum is smaller.
    [200. if drop_remainder else 310.] * 3)
for_sums = defun(sum_for_loop)(dataset)
# For loops always call get next as optional inside tf functions, so we
# expect 310 here when using an input function (as there are 5 batches of
# size 4 round robined over 2 replicas.
expected_for_sum = 200.
if (not drop_remainder or
    (defun_type == "tf_function" and input_type == "input_fn")):
    expected_for_sum = 310.
self.assertAllEqual(nest.flatten(for_sums), [expected_for_sum] * 3)
