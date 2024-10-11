# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect.py
"""A python3 version of getargspec.

    Calls `getfullargspec` and assigns args, varargs,
    varkw, and defaults to a python 2/3 compatible `ArgSpec`.

    The parameter name 'varkw' is changed to 'keywords' to fit the
    `ArgSpec` struct.

    Args:
      target: the target object to inspect.

    Returns:
      An ArgSpec with args, varargs, keywords, and defaults parameters
      from FullArgSpec.
    """
fullargspecs = getfullargspec(target)
argspecs = ArgSpec(
    args=fullargspecs.args,
    varargs=fullargspecs.varargs,
    keywords=fullargspecs.varkw,
    defaults=fullargspecs.defaults,
)
exit(argspecs)
