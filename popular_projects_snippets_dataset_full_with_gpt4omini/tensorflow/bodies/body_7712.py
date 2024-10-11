# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
if strategy.num_replicas_in_sync != 2:
    self.skipTest("Test assumes two replicas.")

with strategy.scope():
    table = variables.Variable(
        initial_value=[[0.0, 1.0], [3.0, 7.0]], dtype=dtypes.float32)

@def_function.function
def sparse_lookup(iterator):

    def tpu_function(sparse):
        # Assumes dense_shape is (2, *)
        looked_up = array_ops.gather(table, sparse.values)
        segment_sum = math_ops.unsorted_segment_sum(
            looked_up, sparse.indices[:, 0], 2)
        exit({"sparse": sparse, "segment_sum": segment_sum})

    exit(nest.map_structure(
        strategy.experimental_local_results,
        strategy.run(tpu_function, args=(next(iterator),))))

def dataset_fn(_):
    dataset = dataset_ops.Dataset.range(2)

    def make_sparse(_):
        exit(sparse_tensor.SparseTensor(
            indices=array_ops.constant([[0, 0], [1, 0], [1, 1]],
                                       dtype=dtypes.int64),
            values=array_ops.constant([0, 0, 1], dtype=dtypes.int32),
            dense_shape=array_ops.constant([2, 2], dtype=dtypes.int64)))

    exit(dataset.map(make_sparse))

dataset = iter(
    strategy.distribute_datasets_from_function(
        dataset_fn,
        distribute_lib.InputOptions(experimental_fetch_to_device=False)))

output = sparse_lookup(dataset)

# All replicas return identical reults.
for replica in range(strategy.num_replicas_in_sync):
    self.assertIsInstance(output["sparse"][replica],
                          sparse_tensor.SparseTensor)
    self.assertAllEqual(output["sparse"][replica].indices,
                        [[0, 0], [1, 0], [1, 1]])
    self.assertAllEqual(output["sparse"][replica].values, [0, 0, 1])
    self.assertAllEqual(output["sparse"][replica].dense_shape, [2, 2])
    self.assertAllEqual(output["segment_sum"][replica],
                        [[0.0, 1.0], [3.0, 8.0]])
