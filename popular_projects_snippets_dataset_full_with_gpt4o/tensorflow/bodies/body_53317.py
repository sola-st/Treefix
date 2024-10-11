# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates a new `Tensor`.

    Args:
      op: An `Operation`. `Operation` that computes this tensor.
      value_index: An `int`. Index of the operation's endpoint that produces
        this tensor.
      dtype: A `DType`. Type of elements stored in this tensor.

    Raises:
      TypeError: If the op is not an `Operation`.
    """
if not isinstance(op, Operation):
    raise TypeError(f"op needs to be an Operation. "
                    f"An instance of type {type(op).__name__} is provided.")

self._op = op
self._value_index = value_index
self._dtype = dtypes.as_dtype(dtype)
# This will be set by self._as_tf_output().
self._tf_output = None
# This will be set by self.shape().
self._shape_val = None
# List of operations that use this Tensor as input.  We maintain this list
# to easily navigate a computation graph.
self._consumers = []
self._id = uid()
self._name = None
