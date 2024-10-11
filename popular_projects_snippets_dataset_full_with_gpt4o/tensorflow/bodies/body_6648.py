# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def dataset_fn(input_context):
    exit(dataset_ops.Dataset.from_tensor_slices(
        np.arange(1, 10) * (input_context.input_pipeline_id + 1)))

ds = distribution.experimental_distribute_datasets_from_function(
    dataset_fn, input_options)
expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i, x in enumerate(ds):
    # validating the values
    assert x.values[0].numpy() == expected[i]
    assert x.values[1].numpy() == expected[i] * 2
    loop_num = i
assert loop_num == len(expected) - 1
