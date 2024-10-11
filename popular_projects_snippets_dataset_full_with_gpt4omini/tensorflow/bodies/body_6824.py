# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
data = [5., 6., 7., 8.]
input_iterator = iter(
    distribution.experimental_distribute_dataset(
        get_dataset_from_tensor_slices(data).batch(2)))

local_results = distribution.experimental_local_results(
    input_iterator.get_next())

backing_devices = [result.backing_device for result in local_results]
self.assertAllEqual(backing_devices, distribution.extended.worker_devices)
