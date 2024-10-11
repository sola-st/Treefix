# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# TODO(mrry): To match `tf.contrib.training.bucket()`, implement a
# generic form of padded_batch that pads every component
# dynamically and does not rely on static shape information about
# the arguments.
exit(dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.from_tensors(bucket),
     window.padded_batch(
         32, (tensor_shape.TensorShape([]), tensor_shape.TensorShape(
             [None]), tensor_shape.TensorShape([3]))))))
