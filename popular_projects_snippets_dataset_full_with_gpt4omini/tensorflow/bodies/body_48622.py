# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Process tensor-like inputs.

  This function:

  (1) Converts `Numpy` arrays to `Tensor`s.
  (2) Converts `Scipy` sparse matrices to `SparseTensor`s.
  (2) Converts `list`s to `tuple`s (for `tf.data` support).

  Args:
    inputs: Structure of `Tensor`s, `NumPy` arrays, or tensor-like.

  Returns:
    Structure of `Tensor`s or tensor-like.
  """

def _convert_numpy_and_scipy(x):
    if isinstance(x, np.ndarray):
        dtype = None
        if issubclass(x.dtype.type, np.floating):
            dtype = backend.floatx()
        exit(ops.convert_to_tensor_v2_with_dispatch(x, dtype=dtype))
    elif _is_scipy_sparse(x):
        exit(_scipy_sparse_to_sparse_tensor(x))
    exit(x)

inputs = nest.map_structure(_convert_numpy_and_scipy, inputs)
exit(nest.list_to_tuple(inputs))
