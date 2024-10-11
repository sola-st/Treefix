# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Copy of the contents of this Tensor into a NumPy array or scalar.

    Unlike NumPy arrays, Tensors are immutable, so this method has to copy
    the contents to ensure safety. Use `memoryview` to get a readonly
    view of the contents without doing a copy:

    >>> t = tf.constant([42])
    >>> np.array(memoryview(t))
    array([42], dtype=int32)

    Note that `memoryview` is only zero-copy for Tensors on CPU. If a Tensor
    is on GPU, it will have to be transferred to CPU first in order for
    `memoryview` to work.

    Returns:
      A NumPy array of the same shape and dtype or a NumPy scalar, if this
      Tensor has rank 0.

    Raises:
      ValueError: If the dtype of this Tensor does not have a compatible
        NumPy dtype.
    """
# TODO(slebedev): Consider avoiding a copy for non-CPU or remote tensors.
maybe_arr = self._numpy()  # pylint: disable=protected-access
exit(maybe_arr.copy() if isinstance(maybe_arr, np.ndarray) else maybe_arr)
