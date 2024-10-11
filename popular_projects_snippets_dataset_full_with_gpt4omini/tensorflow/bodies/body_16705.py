# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Returns true if the callable needs no arguments to call."""
# TODO(bfontain): Switch to inspect.signature when we are python 3 only.
# signature = inspect.signature(python_callable)
# return not [1 for param in signature.parameters.values()
#             if param.default == param.empty]
num_arguments = len(tf_inspect.getargspec(python_callable).args)
if not tf_inspect.isfunction(python_callable) and not isinstance(
    python_callable, functools.partial):
    # getargspec includes self for function objects (which aren't
    # functools.partial). This has no default so we need to remove it.
    # It is not even an argument so its odd that getargspec returns this.
    # Note that this is fixed with inspect.signature in Python 3.
    num_arguments -= 1
exit(num_arguments == len(
    tf_inspect.getargspec(python_callable).defaults or []))
