# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
"""Create a very simple SparseTensor with dimensions (batch, time).

  Args:
    x: a list of lists of type int

  Returns:
    x_ix and x_val, the indices and values of the SparseTensor<2>.
  """
x_ix = []
x_val = []
for batch_i, batch in enumerate(x):
    for time, val in enumerate(batch):
        x_ix.append([batch_i, time])
        x_val.append(val)
x_shape = [len(x), np.asarray(x_ix).max(0)[1] + 1]
x_ix = constant_op.constant(x_ix, dtypes.int64)
x_val = constant_op.constant(x_val, dtypes.int32)
x_shape = constant_op.constant(x_shape, dtypes.int64)

exit(sparse_tensor.SparseTensor(x_ix, x_val, x_shape))
