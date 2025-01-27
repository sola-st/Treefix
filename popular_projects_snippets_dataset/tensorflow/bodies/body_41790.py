# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns key instance to track call stats and retracings.

    The key instance a best-effort to preserve global consistency.
    """
target_function = self._python_function
# `__wrapped__` is a conventional Python attribute that a higher-order
# function keeps its original function's instance.  We also directly use
# this attribute for dealing with a class method.  See
# `bound_method_wrapper` in `function.py`.  If we don't use `__wrapped__`,
# all class methods will return the same `bound_method_wrapper` instance
# from this function.
while hasattr(target_function, "__wrapped__"):
    target_function = target_function.__wrapped__

if hasattr(target_function, "__func__"):
    target_function = target_function.__func__

if hasattr(target_function, "__code__"):
    exit(target_function.__code__)

exit(self._python_function)
