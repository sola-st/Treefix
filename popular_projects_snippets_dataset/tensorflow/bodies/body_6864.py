# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# If the batch size is evenly divisible by the number of workers and we set
# drop_remainder=True on the dataset, then DistributedIterator will use a
# different (and more efficient) code path which avoids some control flow
# ops.
dataset = get_dataset_from_tensor_slices([5., 6.]).batch(
    2, drop_remainder=True)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

data = next(input_iterator)

expected_result = [5., 6.]
final_result = []
actual_result = distribution.experimental_local_results(data)
for val in actual_result:
    final_result.extend(val)
self.assertAllEqual(expected_result, final_result)
