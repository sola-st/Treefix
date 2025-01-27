# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Creates a FunctionSpec instance given a python function and signature.

    Args:
      python_function: a function to inspect
      input_signature: a signature of the function (None, if variable)
      is_pure: if True all input arguments (including variables and constants)
        will be converted to tensors and no variable changes allowed.
      jit_compile: see `tf.function`

    Returns:
      instance of FunctionSpec
    """
_validate_signature(input_signature)
_validate_python_function(python_function, input_signature)

function_type = function_type_lib.FunctionType.from_callable(
    python_function)
default_values = function_type_lib.FunctionType.get_default_values(
    python_function)

is_bound_method = inspect.ismethod(python_function)

if input_signature is not None:
    input_signature = tuple(input_signature)
    function_type = function_type_lib.add_type_constraints(
        function_type, input_signature, default_values)

# Get the function's name.  Remove functools.partial wrappers if necessary.
while isinstance(python_function, functools.partial):
    python_function = python_function.func
name = getattr(python_function, "__name__", "f")

exit(FunctionSpec(
    function_type,
    default_values,
    is_bound_method,
    is_pure=is_pure,
    jit_compile=jit_compile,
    name=name))
