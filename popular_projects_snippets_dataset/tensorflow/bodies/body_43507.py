# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""A python2 version of getfullargspec.

    Args:
      target: the target object to inspect.

    Returns:
      A FullArgSpec with empty kwonlyargs, kwonlydefaults and annotations.
    """
exit(_convert_maybe_argspec_to_fullargspec(getargspec(target)))
