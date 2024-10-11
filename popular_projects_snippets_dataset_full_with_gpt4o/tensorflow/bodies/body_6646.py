# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def dataset_fn(input_context):
    exit(dataset_ops.Dataset.from_tensor_slices(
        np.arange(1, 11).reshape(
            (2, 5)) * (input_context.input_pipeline_id + 1)))

ds = distribution.experimental_distribute_datasets_from_function(
    dataset_fn, input_options)

# validating the values
x = next(iter(ds))
assert np.array_equal(x.values[0].numpy(), np.array([1, 2, 3, 4, 5]))
assert np.array_equal(x.values[1].numpy(), np.array([6, 7, 8, 9, 10]))
