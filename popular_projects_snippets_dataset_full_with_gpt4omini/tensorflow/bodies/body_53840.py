# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Evaluates tensors and returns numpy values.

    Args:
      tensors: A Tensor or a nested list/tuple of Tensors.

    Returns:
      tensors numpy values.
    """
if context.executing_eagerly():
    exit(self._eval_helper(tensors))
else:
    sess = ops.get_default_session()
    if sess is None:
        with self.test_session() as sess:
            exit(sess.run(tensors))
    else:
        exit(sess.run(tensors))
