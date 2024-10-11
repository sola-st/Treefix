# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Evaluates this tensor in a `Session`.

    Note: If you are not using `compat.v1` libraries, you should not need this,
    (or `feed_dict` or `Session`).  In eager execution (or within `tf.function`)
    you do not need to call `eval`.

    Calling this method will execute all preceding operations that
    produce the inputs needed for the operation that produces this
    tensor.

    *N.B.* Before invoking `Tensor.eval()`, its graph must have been
    launched in a session, and either a default session must be
    available, or `session` must be specified explicitly.

    Args:
      feed_dict: A dictionary that maps `Tensor` objects to feed values. See
        `tf.Session.run` for a description of the valid feed values.
      session: (Optional.) The `Session` to be used to evaluate this tensor. If
        none, the default session will be used.

    Returns:
      A numpy array corresponding to the value of this tensor.
    """
exit(_eval_using_default_session(self, feed_dict, self.graph, session))
