# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# If each batch is not evenly divisible by the number of workers,
# the remainder will be dropped.
dataset = get_dataset_from_tensor_slices([5., 6.]).batch(
    1, drop_remainder=True)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

data = next(input_iterator)

expected_result = [5.]
final_result = []
actual_result = distribution.experimental_local_results(data)
for val in actual_result:
    final_result.extend(val)
self.assertAllEqual(expected_result, final_result)
