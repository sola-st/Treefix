# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
exit(dataset_ops.Dataset.from_generator(
    my_generator, (dtypes.int64, dtypes.int64),
    (tensor_shape.TensorShape([]), tensor_shape.TensorShape([10]))))
