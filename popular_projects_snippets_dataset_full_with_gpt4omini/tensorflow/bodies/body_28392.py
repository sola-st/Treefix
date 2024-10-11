# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
exit(dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.from_tensors(bucket),
     window.padded_batch(
         32, {
             "x": tensor_shape.TensorShape([]),
             "y": tensor_shape.TensorShape([None]),
             "z": tensor_shape.TensorShape([3])
         }))))
