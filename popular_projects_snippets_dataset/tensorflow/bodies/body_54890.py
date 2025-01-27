# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
    concatenate_fn(
        tensor_shape.TensorShape([1, 2]), tensor_shape.TensorShape([3, 4])))
tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
    concatenate_fn(
        tensor_shape.TensorShape([1, 2]), tensor_shape.TensorShape(None)))
tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
    concatenate_fn(
        tensor_shape.TensorShape(None), tensor_shape.TensorShape([3, 4])))
tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
    concatenate_fn(
        tensor_shape.TensorShape(None), tensor_shape.TensorShape(None)))
