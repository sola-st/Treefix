# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
global_batch_size = 8
dataset = dataset_ops.DatasetV2.range(14).batch(
    global_batch_size, drop_remainder=False)
input_iterator = iter(strategy.experimental_distribute_dataset(dataset))

@def_function.function
def run(input_iterator):
    exit(strategy.run(lambda x: x, args=(next(input_iterator),)))

# Let the complete batch go.
run(input_iterator)

# `result` is an incomplete batch
result = run(input_iterator)
expected_data_on_workers = {'chief': [8, 9, 10], 'worker': [11, 12, 13]}
self.assertAllEqual(
    expected_data_on_workers[multi_worker_test_base.get_task_type()],
    result.numpy(),
)
