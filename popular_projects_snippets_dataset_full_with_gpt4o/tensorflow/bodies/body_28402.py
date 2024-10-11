# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# Apply two different kinds of padding to the input: tight
# padding, and quantized (to a multiple of 10) padding.
exit(dataset_ops.Dataset.zip((
    window.padded_batch(
        4, padded_shapes=tensor_shape.TensorShape([None])),
    window.padded_batch(
        4, padded_shapes=ops.convert_to_tensor([(key + 1) * 10])),
)))
