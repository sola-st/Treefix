# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns a _FuncGraph generated from `func`.

  Args:
    func: A Python callable which constructs a TF function body. The arguments
      must correspond to `arg_types`. Returns a value or list/tuple of values.
      No returned value can be None.
    arg_names: A sequence of strings for the function argument names.
    arg_types: A sequence of the function's argument types.
    name: The function name. If None, the name is derived from `func`.
    capture_by_value: boolean. If True, captured values will be copied into the
      function body.
    device: device name or function.
    colocation_stack: A colocation stack (list) the _FuncGraph should use.
    container: A container name the _FuncGraph should start with.
    collections_ref: A reference to a collections dict the _FuncGraph should
      use internally.
    arg_shapes: A sequence of the function's argument shapes.
    allowlisted_stateful_ops: A set of ops that if stateful we ignore and
      re-create.
    capture_resource_var_by_value: Boolean (defaults to True). If False,
      captured resource variable returns the handle instead of value.

  Returns:
    A _FuncGraph.

  Raises:
    ValueError: if func returns None.
  """
if not name:
    name = function_utils.get_func_name(func)
func_graph = _FuncGraph(name, capture_by_value, allowlisted_stateful_ops,
                        capture_resource_var_by_value)

with func_graph.as_default(), ops.device(device):
    # pylint: disable=protected-access
    if collections_ref is not None:
        func_graph._collections = collections_ref
    if container is not None:
        func_graph._container = container
    if colocation_stack is not None:
        func_graph._colocation_stack = colocation_stack
    # pylint: enable=protected-access

    if arg_shapes is None:
        arg_shapes = [None] * len(arg_types)

    # Create placeholders for the function arguments.
    for (argname, argtype, argshape) in zip(arg_names, arg_types, arg_shapes):
        argholder = array_ops.placeholder(argtype, shape=argshape, name=argname)
        func_graph.inputs.append(argholder)
    # Call func and gather the output tensors.
    with vs.variable_scope("", custom_getter=func_graph.getvar):
        outputs = func(*func_graph.inputs)

    # There is no way of distinguishing between a function not returning
    # anything and a function returning None in Python.
    # We need to allow the former and ideally want to forbid the latter as
    # it is most likely user error.
    # TODO(iga): Consider adding a @NoOutput decorator on top of @Defun to
    # allow users to explicitly mark the function as not returning anything.
    # For now, we allow a single None return and interpret it as a function
    # with no output.
    if outputs is None:
        outputs = []
    else:
        # If func only returned one value, make it a tuple.
        if not isinstance(outputs, (list, tuple)):
            outputs = (outputs,)
        if any(_ is None for _ in outputs):
            raise ValueError(f"Function {name} can not return None.")
    # Ensures each output is a Tensor in the function graph.
    outputs = [ops.convert_to_tensor(t) for t in outputs]
    outputs = [func_graph.capture(t) if t.graph is not func_graph else t
               for t in outputs]
    func_graph.outputs = outputs
exit(func_graph)
