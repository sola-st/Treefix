# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates _DefinedFunction.

    Args:
      func:  A python callable which constructs a tf function body.
      argnames: A list of strings for function argument names.
      input_types: The function's argument types. Can be a tuple, list of
        tf data types.
      func_name: The function name. Defaults to None, in which derives from
        'func'.
      grad_func: This function's gradient function, if not None. Defaults
        to None.
      python_grad_func: A python callable implementing the gradient of
        the function python-side.
      out_names: An optional list of strings for the function return value
        names.
      shape_func: An optional function mapping an op to a list of static
        output shapes.
      capture_by_value: Boolean (defaults to False). If True, captured values
        will be copied into the function body.
      allowlisted_stateful_ops: A set of ops that if stateful we ignore and
        copy into the function body, when `capture_by_value` is True.
      capture_resource_var_by_value: Boolean (defaults to True). If False,
        captured resource variable returns the handle instead of value.
      **kwargs: The keyword arguments. **kwargs is passed to every call
        site of this function.

    Raises:
      ValueError: The function definition is invalid.

    """
self._func = func
self._input_types = input_types
self._func_name = func_name
self._grad_func = grad_func
self._python_grad_func = python_grad_func
self._out_names = out_names
self._shape_func = shape_func
self._capture_by_value = capture_by_value
self._allowlisted_stateful_ops = allowlisted_stateful_ops
if self._allowlisted_stateful_ops is None:
    self._allowlisted_stateful_ops = set()
self._capture_resource_var_by_value = capture_resource_var_by_value
self._extra_kwargs = kwargs
# Constructed only when C API is disabled, lazily
self._definition = None
# Constructed only when C API is enabled, lazily
self._c_func = None
self._function_deleter = None
self._sub_functions = {}  # Constructed with _definition or _c_func
# pylint: disable=protected-access
device_funcs = ops.get_default_graph()._device_functions_outer_to_inner
# pylint: enable=protected-access

# Get the innermost device if possible.
self._caller_device = device_funcs[-1] if device_funcs else None

# Cached OpDef for this function. When C API is enabled, this is
# the only part of FunctionDef that we cache in Python. When C API
# is disabled the whole _definition is available and this is simply
# another reference to _definition.signature
self._op_def = None

assert isinstance(input_types, (list, tuple))
self._arg_types = input_types
self._arg_names = [argnames[i] if i < len(argnames) else ("arg%d" % i)
                   for i in range(len(input_types))]
