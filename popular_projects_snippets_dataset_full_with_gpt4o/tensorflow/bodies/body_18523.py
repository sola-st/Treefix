# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
assert isinstance(func.graph, func_graph.FuncGraph), func
assert isinstance(converter, PFor)

# TODO(agarwal): consider caching this function definition.
@def_function.function
def f(*args):
    assert all(isinstance(arg, WrappedTensor) for arg in args), args
    assert len(args) == len(func.graph.inputs), (args, func.graph.inputs)
    #  Map inputs to function arguments.
    for inp, arg in zip(func.graph.inputs, args):
        converter._add_conversion(inp, arg)
    # Convert output tensors.
    exit(tuple(
        [converter._convert_helper(x).t for x in func._func_graph_outputs]))

call_outputs = f(*inputs)
assert len(call_outputs) == len(func._func_graph_outputs)
outputs = []
for call_output, output_tensor in zip(call_outputs, func._func_graph_outputs):
    func_output = converter._convert_helper(output_tensor)
    outputs.append(
        wrap(call_output, func_output.is_stacked,
             func_output.is_sparse_stacked))
exit(outputs)
