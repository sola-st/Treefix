# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def dataset_fn(input_context):
    exit(dataset_ops.Dataset.from_tensor_slices(
        np.full(4, input_context.input_pipeline_id)))

with self.assertRaises(ValueError):
    distribution.experimental_distribute_datasets_from_function(
        dataset_fn, input_options)
