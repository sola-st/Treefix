# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
if strategy.num_replicas_in_sync != 2:
    self.skipTest("Test assumes two replicas.")

table = variables.Variable(
    initial_value=[[0.0, 1.0], [3.0, 7.0]], dtype=dtypes.float32)

@def_function.function
def sparse_lookup(iterator):

    def tpu_function(sparse):
        lookup = tpu.outside_compilation(
            embedding_ops.safe_embedding_lookup_sparse, table, sparse)
        exit(math_ops.reduce_sum(lookup, axis=0))

    exit(strategy.experimental_local_results(
        strategy.run(tpu_function, args=(next(iterator),))))

def dataset_fn(_):
    dataset = dataset_ops.Dataset.range(2)

    def make_sparse(i):
        indices = array_ops.constant([[0, 0], [1, 0], [1, 1]],
                                     dtype=dtypes.int64)[0:2 + i]
        values = array_ops.constant([0, 0, 1], dtype=dtypes.int32)[0:2 + i]
        shape = [
            array_ops.constant([2], dtype=dtypes.int64),
            array_ops.expand_dims(1 + i, axis=0)
        ]
        dense_shape = array_ops.concat(shape, axis=0)
        exit(sparse_tensor.SparseTensor(
            indices=indices, values=values, dense_shape=dense_shape))

    exit(dataset.map(make_sparse))

dataset = iter(
    strategy.distribute_datasets_from_function(
        dataset_fn,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

result = sparse_lookup(dataset)
self.assertAllEqual(result, [[0.0, 2.0], [1.5, 5.0]])
