# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
exit(self._apply_sparse_shared(
    grad.values,
    var,
    grad.indices,
    lambda x, i, v: state_ops.scatter_add(  # pylint: disable=g-long-lambda
        x,
        i,
        v,
        use_locking=self._use_locking)))
