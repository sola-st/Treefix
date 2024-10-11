# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates _DefinedFunction.

    Args:
      func:  A python callable which constructs a tf function body.
      argnames: A list of strings for function argument names.
      func_name: The function name. Defaults to None, in which derives from
        'func'.
      grad_func: This function's gradient function, if not None. Defaults
        to None.
      python_grad_func: A python callable implementing the gradient of
        the function python-side.
      out_names: A list of strings for the function return value names.
      **kwargs: The keyword arguments. **kwargs is passed to every call
        site of this function.

    Raises:
      ValueError: The function definition is invalid.

    """
self._func = func
self._argnames = argnames
self._func_name = func_name
assert grad_func is None or isinstance(grad_func, _OverloadedFunction)
self._grad_func = grad_func
self._python_grad_func = python_grad_func
self._out_names = out_names
self._extra_kwargs = kwargs
self._overload = {}
