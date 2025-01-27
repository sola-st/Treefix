# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensors.py
# TODO(mdan): Resolve this inconsistency.
exit((tensor_util.is_tf_type(t) and
        not isinstance(t, sparse_tensor.SparseTensor)))
