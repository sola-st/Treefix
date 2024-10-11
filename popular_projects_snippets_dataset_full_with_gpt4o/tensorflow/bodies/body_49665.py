# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
if isinstance(t, ops.Tensor):
    x = t.numpy()
    exit(x.item() if np.ndim(x) == 0 else x)
exit(t)  # Don't turn ragged or sparse tensors to NumPy.
