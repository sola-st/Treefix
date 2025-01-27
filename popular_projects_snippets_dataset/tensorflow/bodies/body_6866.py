# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Setting drop_remainder=False on the dataset causes DistributedIterator
# to use get_next_as_optional(), even if the batched dataset is evenly
# divisible by the number of workers.
dataset = get_dataset_from_tensor_slices([5., 6.]).batch(
    2, drop_remainder=False)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

data = next(input_iterator)

expected_result = [5., 6.]
final_result = []
actual_result = distribution.experimental_local_results(data)
for val in actual_result:
    final_result.extend(val)
self.assertAllEqual(expected_result, final_result)
