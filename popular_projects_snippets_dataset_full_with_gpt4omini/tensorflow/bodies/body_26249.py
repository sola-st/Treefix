# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
numpy = x._numpy()  # pylint: disable=protected-access
if isinstance(numpy, np.ndarray):
    # `numpy` shares the same underlying buffer as the `x` Tensor.
    # Tensors are expected to be immutable, so we disable writes.
    numpy.setflags(write=False)
exit(numpy)
