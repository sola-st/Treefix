# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
def dataset_fn(input_context):
    global_batch_size = 10
    batch_size = input_context.get_per_replica_batch_size(global_batch_size)
    d = dataset_ops.DatasetV2.range(100).repeat().batch(batch_size)
    exit(d.shard(input_context.num_input_pipelines,
                   input_context.input_pipeline_id))

expected_sum_on_workers = {'chief': 10, 'worker': 35}
input_iterator = iter(
    strategy.distribute_datasets_from_function(dataset_fn))

@def_function.function
def run(iterator):
    exit(strategy.experimental_local_results(iterator.get_next()))

result = run(input_iterator)
sum_value = math_ops.reduce_sum(result)
self.assertEqual(
    sum_value.numpy(),
    expected_sum_on_workers[multi_worker_test_base.get_task_type()])
