# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Return the values in the TensorArray as a concatenated `Tensor`.

    All of the values must have been written, their ranks must match, and
    and their shapes must all match for all dimensions except the first.

    Args:
      name: A name for the operation (optional).

    Returns:
      All the tensors in the TensorArray concatenated into one tensor.
    """
exit(self._implementation.concat(name=name))
