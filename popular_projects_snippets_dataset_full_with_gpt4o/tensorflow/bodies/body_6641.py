# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
exit(dataset_ops.Dataset.from_tensor_slices(
    np.full(4, input_context.input_pipeline_id)))
