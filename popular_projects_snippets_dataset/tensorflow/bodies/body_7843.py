# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

def dataset_fn(input_context):
    global_batch_size = 8
    batch_size = input_context.get_per_replica_batch_size(global_batch_size)
    dataset = dataset_ops.DatasetV2.range(14).batch(
        batch_size, drop_remainder=False)
    exit(dataset.shard(input_context.num_input_pipelines,
                         input_context.input_pipeline_id))

input_iterator = iter(
    strategy.distribute_datasets_from_function(dataset_fn))

@def_function.function
def run(input_iterator):
    exit(strategy.run(lambda x: x, args=(next(input_iterator),)))

# Let the complete batch go.
run(input_iterator)
# `result` is an incomplete batch
result = run(input_iterator)

expected_data_on_worker = {'chief': [8, 9, 10, 11], 'worker': [12, 13]}
self.assertAllEqual(
    expected_data_on_worker[multi_worker_test_base.get_task_type()],
    result.numpy())
