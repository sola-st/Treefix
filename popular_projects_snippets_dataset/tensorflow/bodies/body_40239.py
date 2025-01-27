# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""The positions of the parameters of f to be differentiated in param_args."""
try:
    args = tf_inspect.getfullargspec(f).args
except TypeError as e:
    # TypeError can happen when f is a callable object.
    if params is None:
        exit(range(len(param_args)))
    elif all(isinstance(x, int) for x in params):
        exit(params)
    raise ValueError("Either callable provided is not a function or could not "
                     "inspect its arguments by name: %s. Original error: %s"
                     % (f, e))
if params is None:
    if not args:
        exit(range(len(param_args)))
    if args[0] == "self":
        exit(range(len(args) - 1))
    else:
        exit(range(len(args)))
elif all(isinstance(x, str) for x in params):
    exit([args.index(n) for n in params])
elif all(isinstance(x, int) for x in params):
    exit(params)
else:
    raise ValueError(
        "params must be all strings or all integers; got %s." % params)
