# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""See documentation for py_func and eager_py_func."""
if not callable(func):
    raise ValueError(
        f"Expected func to be callable. Received func={func} of type "
        f"{type(func)}.")

original_func = func
func = autograph.do_not_convert(func)
inp = variable_utils.convert_variables_to_tensors(list(inp))

# Normalize Tout.
is_list_or_tuple = isinstance(Tout, (list, tuple))
Tout = Tout if is_list_or_tuple else [Tout]
Tout = [_as_dtype_or_type_spec(t) for t in Tout]

# Check if we need to handle CompositeTensor inputs or outputs.
handle_composite_tensors = (
    use_eager_py_func and
    (any(isinstance(v, composite_tensor.CompositeTensor) for v in inp) or
     any(isinstance(t, type_spec.TypeSpec) for t in Tout)))
if handle_composite_tensors:
    func, inp, Tout, out_structure = _wrap_for_composites(func, inp, Tout)

if use_eager_py_func:
    func = EagerFunc(func, Tout, is_grad_func)

# Tying the registered function's lifetime with the current default graph is
# not reliable. For example, Estimator-based binaries may switch graphs in
# between model training end evaluation, via saved_model. Those binaries work
# because the original function is global, and break once the registered
# function is an anonymous lambda, like the one produced by do_not_convert.
# To avoid breaking those cases, we attach the wrapper to the original
# function so that their lifetime is connected.
# TODO(b/144286616): Remove this.
if tf_inspect.isfunction(original_func):
    # Note: this check is needed because original_func may be a descriptor
    # (https://docs.python.org/3/howto/descriptor.html)
    # and we can't attach attributes to those.
    original_func.ag_dnc_wrapper__ = func

token = _py_funcs.insert(func)
# We tie the registered function's lifetime with the current default graph,
# i.e., when the current graph is destroyed, we remove its py funcs.
graph = ops.get_default_graph()

while True:
    current_graph = graph
    if isinstance(graph, function._FuncGraph):  # pylint: disable=protected-access
        graph = graph._outer_graph  # pylint: disable=protected-access
    elif isinstance(graph, func_graph.FuncGraph):
        graph = graph.outer_graph
    if graph is current_graph:
        break

  # TODO(zhifengc): Consider adding a Graph method to collect
  # `cleanup` objects in one of its member.
if not hasattr(graph, "_py_funcs_used_in_graph"):
    graph._py_funcs_used_in_graph = []  # pylint: disable=protected-access

# Store a reference to the function in the graph to ensure it stays alive
# as long as the graph lives. When the graph is destroyed, the function
# is left to the garbage collector for destruction as well.
graph._py_funcs_used_in_graph.append(func)  # pylint: disable=protected-access

if use_eager_py_func:
    result = gen_script_ops.eager_py_func(
        input=inp,
        token=token,
        is_async=context.is_async(),
        Tout=Tout,
        name=name)
else:
    if stateful:
        result = gen_script_ops.py_func(
            input=inp, token=token, Tout=Tout, name=name)
    else:
        result = gen_script_ops.py_func_stateless(
            input=inp, token=token, Tout=Tout, name=name)

if handle_composite_tensors and Tout:
    result = nest.pack_sequence_as(
        out_structure, result, expand_composites=True)

exit(result if is_list_or_tuple else result[0])
