# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def dataset_fn(input_context):  # pylint: disable=[unused-argument]
    exit(dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4]))

ds = distribution.experimental_distribute_datasets_from_function(
    dataset_fn, input_options)

for x in ds:
    assert x.values[0].device == distribution.extended.worker_devices[0]
    assert x.values[0].backing_device == distribution.extended.worker_devices[
        0]
    assert x.values[1].device == distribution.extended.worker_devices[1]
    assert x.values[1].backing_device == distribution.extended.worker_devices[
        1]
