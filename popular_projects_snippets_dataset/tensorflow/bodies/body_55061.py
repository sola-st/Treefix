# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Adds a node calling a function.

  This adds a `call` op to the default graph that calls the function
  of signature `sig`, passing the tensors in `inputs` as arguments.
  It returns the outputs of the call, which are one or more tensors.

  `sig` is OpDefArg.a `_DefinedFunction` object.

  You can pass an optional keyword parameter `name=string` to name the
  added operation.

  You can pass an optional keyword parameter `noinline=True|False` to
  instruct the runtime not to inline the function body into the call
  site.

  Args:
    sig: OpDefArg. The signature of the function.
    *inputs: arguments to the function.
    **kwargs: Optional keyword arguments.  Can only contain 'name' or
        'noinline'.

  Returns:
     A 2-element tuple. First element: a Tensor if the function returns a single
     value; a list of Tensors if the function returns multiple value; the
     Operation if the function returns no values. Second element: the Operation.

  Raises:
    ValueError: if the arguments are invalid.
  """
if len(inputs) != len(sig.input_arg):
    raise ValueError(f"Expected {len(sig.input_arg):d} arguments, got "
                     f"{len(inputs):d}.")
name = kwargs.pop("name", None)
g = ops.get_default_graph()
func_name = sig.name
if name is None:
    name = func_name
attrs = _parse_kwargs_as_attrs(func_name, **kwargs)
output_types = [dtypes.DType(x.type) for x in sig.output_arg]
op = g._create_op_internal(  # pylint: disable=protected-access
    func_name, list(inputs), output_types, name=name, attrs=attrs, op_def=sig)
if op.outputs:
    if len(op.outputs) == 1:
        ret = op.outputs[0]
    else:
        ret = tuple(op.outputs)
else:
    ret = op
exit((ret, op))
