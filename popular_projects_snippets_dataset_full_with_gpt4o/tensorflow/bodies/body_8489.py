# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
# Test for TPU only since it can't be tested via testAllGatherDiffShape*
if not _is_tpu_strategy(strategy):
    self.skipTest('Test for TPU only. For other strategies case already'
                  ' covered in other tests')

data = [[1], [2], [3], [4], [5], [6], [7], [8]]

axis = 0
dataset = dataset_ops.DatasetV2.from_tensor_slices(data).batch(8)
input_iterator = iter(strategy.experimental_distribute_dataset(dataset))

@def_function.function
def replica_fn(per_replica_value):
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather(array_ops.identity(per_replica_value), axis=axis))

result = strategy.experimental_local_results(
    strategy.run(replica_fn, args=(next(input_iterator),)))

expected_result = [data] * _get_num_replicas_per_client(strategy)
self.assertAllClose(expected_result, result)
