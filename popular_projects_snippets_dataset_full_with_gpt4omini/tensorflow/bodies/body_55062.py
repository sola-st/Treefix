# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates a _DefinedFunction initialized from a FunctionDef proto.

  Args:
    fdef: a FunctionDef
    grad_func: a _DefinedFunction or None

  Returns:
    A _DefinedFunction representing fdef
  """
# TODO(iga): This method does major surgery on _DefinedFunction.
# Make it a named constructor using @classmethod of _DefinedFunction.

# The Python callable is only needed to create a FunctionDef. Since we have
# the FunctionDef here, we don't need to set _DefinedFunction._func (nor do we
# have access to such a callable here).
func = None
argnames = [arg.name for arg in fdef.signature.input_arg]
input_types = tuple(
    dtypes.as_dtype(arg.type) for arg in fdef.signature.input_arg)
func_name = fdef.signature.name
# Note: FunctionDefs do not include python gradient functions, so if the
# original _DefinedFunction included one it will not be reflected here.
python_grad_func = None
out_names = [arg.name for arg in fdef.signature.output_arg]
result = _DefinedFunction(func, argnames, input_types, func_name, grad_func,
                          python_grad_func, out_names)
# pylint: disable=protected-access
serialized = fdef.SerializeToString()
c_func = c_api.TF_FunctionImportFunctionDef(serialized)
result._c_func = c_api_util.ScopedTFFunction(c_func, func_name)
result._extra_inputs = []
result._op_def = fdef.signature
# pylint: enable=protected-access

exit(result)
