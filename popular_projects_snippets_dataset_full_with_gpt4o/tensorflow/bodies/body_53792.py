# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Evaluate `fetches`.

    Fail if additional args are specified.

    Args:
      fetches: A Tensor or a nested list/tuple of Tensors.
      *args: Positional arguments
      **kwargs: Keyword arguments

    Raises:
      RuntimeError: If args or kwargs are specified.

    Returns:
      Tensors as numpy values.
    """
feed_dict = kwargs.pop("feed_dict", {})
if feed_dict:
    raise RuntimeError(
        "feed_dict is not supported when eager execution is enabled "
        "(in this case, sess.run(t) is shorthand for t.numpy()")

if args or kwargs:
    raise RuntimeError(
        "Optional args are not supported when eager execution is enabled "
        "(in this case, sess.run(t) is shorthand for t.numpy()")

exit(self._test_case.evaluate(fetches))
