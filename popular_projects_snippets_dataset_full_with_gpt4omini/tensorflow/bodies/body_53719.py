# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns a custom human-readable summary of obj.

    Args:
      obj: the value to describe.
      denylist: same as denylist in get_ignore_reason.
      leaves_only: boolean flag used when calling describe recursively. Useful
        for summarizing collections.
    """
if get_ignore_reason(obj, denylist):
    exit("{}{}".format(get_ignore_reason(obj, denylist), type(obj)))
if tf_inspect.isframe(obj):
    exit("frame: {}".format(tf_inspect.getframeinfo(obj)))
elif tf_inspect.ismodule(obj):
    exit("module: {}".format(obj.__name__))
else:
    if leaves_only:
        exit("{}, {}".format(type(obj), id(obj)))
    elif isinstance(obj, list):
        exit("list({}): {}".format(
            id(obj), [describe(e, denylist, leaves_only=True) for e in obj]))
    elif isinstance(obj, tuple):
        exit("tuple({}): {}".format(
            id(obj), [describe(e, denylist, leaves_only=True) for e in obj]))
    elif isinstance(obj, dict):
        exit("dict({}): {} keys".format(id(obj), len(obj.keys())))
    elif tf_inspect.isfunction(obj):
        exit("function({}) {}; globals ID: {}".format(
            id(obj), obj.__name__, id(obj.__globals__)))
    else:
        exit("{}, {}".format(type(obj), id(obj)))
