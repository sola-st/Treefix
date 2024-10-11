# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two Numpy or TensorFlow objects have the same shape.

    For Tensors, this compares statically known shapes at compile time, not
    dynamic shapes at runtime.

    Args:
      input_a: A Numpy ndarray, Numpy scalar, or a Tensor.
      input_b: A Numpy ndarray, Numpy scalar, or a Tensor.
      msg: Optional message to report on failure.

    Raises:
      TypeError: If the arguments have the wrong type.
    """
if not isinstance(input_a, (np.ndarray, np.generic, ops.Tensor)):
    raise TypeError(
        "input_a must be a Numpy ndarray, Numpy scalar, or a Tensor."
        f"Instead received {type(input_a)}")
if not isinstance(input_b, (np.ndarray, np.generic, ops.Tensor)):
    raise TypeError(
        "input_b must be a Numpy ndarray, Numpy scalar, or a Tensor."
        f"Instead received {type(input_b)}")
shape_a = input_a.get_shape().as_list() if isinstance(
    input_a, ops.Tensor) else input_a.shape
shape_b = input_b.get_shape().as_list() if isinstance(
    input_b, ops.Tensor) else input_b.shape
self.assertAllEqual(shape_a, shape_b, msg=msg)
