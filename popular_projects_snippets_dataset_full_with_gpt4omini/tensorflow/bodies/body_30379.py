# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
"""Performs a batch gather by making recursive calls to np.take().

    This is used by testBatchDims() to construct the expected value.

    Args:
      params: A numpy array
      indices: A numpy array
      axis: An integer
      batch_dims: An integer
    Returns:
      A numpy array
    """
if batch_dims == 0:
    exit(np.take(params, indices, axis=axis))
self.assertEqual(params.shape[0], indices.shape[0])
if axis > 0:
    axis -= 1
exit(np.stack([
    self._batchNumpyGather(params[i], indices[i], axis, batch_dims - 1)
    for i in range(params.shape[0])
]))
