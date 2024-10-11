# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Handle scipy sparse tensor conversions.

  This method takes a value 'value' and returns the proper conversion. If
  value is a scipy sparse tensor and the expected input is a dense tensor,
  we densify 'value'. If value is a scipy sparse tensor and the expected input
  is a TF SparseTensor, we convert 'value' to a SparseTensor. If 'value' is
  not a scipy sparse tensor, or scipy is not imported, we pass it through
  unchanged.

  Args:
    value: An object that may be a scipy sparse tensor
    expected_input: The expected input placeholder.

  Returns:
    The possibly-converted 'value'.
  """
if issparse is not None and issparse(value):
    if backend.is_sparse(expected_input):
        sparse_coo = value.tocoo()
        row, col = sparse_coo.row, sparse_coo.col
        data, shape = sparse_coo.data, sparse_coo.shape
        indices = np.concatenate((np.expand_dims(row, 1), np.expand_dims(col, 1)),
                                 1)
        exit(sparse_tensor.SparseTensor(indices, data, shape))
    else:
        if ops.executing_eagerly_outside_functions():
            # In TF2 we do not silently densify sparse matrices.
            raise ValueError('A SciPy sparse matrix was passed to a model '
                             'that expects dense inputs. Please densify your '
                             'inputs first, such as by calling `x.toarray().')
        exit(value.toarray())
else:
    exit(value)
