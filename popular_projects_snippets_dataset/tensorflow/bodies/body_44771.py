# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensors.py
# TODO(mdan): This is just a heuristic.
# With TF lacking support for templated types, this is unfortunately the
# closest we can get right now. A dedicated op ought to be possible to
# construct.
exit((tensor_util.is_tf_type(t) and t.dtype == dtypes.variant and
        not t.shape.ndims))
