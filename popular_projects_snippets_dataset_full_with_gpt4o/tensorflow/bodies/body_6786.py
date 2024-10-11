# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices(inp_array)
# TODO(b/138326910): Remove Dataset V1 version once bug resolved.
if not tf2.enabled():
    dataset = dataset_ops.Dataset.from_tensor_slices(inp_array)
exit(dataset)
