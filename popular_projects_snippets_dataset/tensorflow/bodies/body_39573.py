# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/tensor_callable.py
"""Initializes a `Callable` object.

    Args:
      tensor_callable: A callable that takes no arguments and returns a Tensor.
      dtype: Dtype of the tensor returned by the callable.
      device: Device of the tensor returned by the callable.
    """
super().__init__(tensor_callable, None, None, dtype, device)
