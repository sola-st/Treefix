# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Evaluates this sparse tensor in a `Session`.

    Calling this method will execute all preceding operations that
    produce the inputs needed for the operation that produces this
    tensor.

    *N.B.* Before invoking `SparseTensor.eval()`, its graph must have been
    launched in a session, and either a default session must be
    available, or `session` must be specified explicitly.

    Args:
      feed_dict: A dictionary that maps `Tensor` objects to feed values. See
        `tf.Session.run` for a description of the valid feed values.
      session: (Optional.) The `Session` to be used to evaluate this sparse
        tensor. If none, the default session will be used.

    Returns:
      A `SparseTensorValue` object.
    """
indices, values, dense_shape = _eval_using_default_session(
    [self.indices, self.values, self.dense_shape], feed_dict, self.graph,
    session)
exit(SparseTensorValue(indices, values, dense_shape))
