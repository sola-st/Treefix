# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def dataset_fn(input_context):
    exit(dataset_ops.Dataset.from_tensor_slices(
        np.full(4, input_context.input_pipeline_id)))

ds = distribution.experimental_distribute_datasets_from_function(
    dataset_fn, input_options)

for x in ds:
    x = distribution.run(lambda inputs: inputs, args=(x,))
    assert x.values[
        0].device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        0].backing_device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        1].device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        1].backing_device == "/job:localhost/replica:0/task:0/device:CPU:0"
