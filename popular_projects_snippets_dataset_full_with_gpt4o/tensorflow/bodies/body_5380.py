# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(values_util.scatter_mul(
    var, sparse_delta, use_locking=use_locking, name=name))
