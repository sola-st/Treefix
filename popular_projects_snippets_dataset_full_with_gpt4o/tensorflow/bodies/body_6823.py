# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
data = [5., 6., 7., 8.]
input_iterator = iter(
    distribution.distribute_datasets_from_function(
        lambda _: get_dataset_from_tensor_slices(data)))

@def_function.function
def run(iterator):
    exit(distribution.experimental_local_results(iterator.get_next()))

local_results = run(input_iterator)
self.assertAllEqual(local_results,
                    data[0:distribution.num_replicas_in_sync])
backing_devices = [result.backing_device for result in local_results]
self.assertAllEqual(backing_devices, distribution.extended.worker_devices)
