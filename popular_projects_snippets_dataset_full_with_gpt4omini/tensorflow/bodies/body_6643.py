# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
exit(dataset_ops.Dataset.from_tensor_slices(
    np.arange(1, 11).reshape(
        (2, 5)) * (input_context.input_pipeline_id + 1)))
