# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
assert all(isinstance(arg, WrappedTensor) for arg in args), args
assert len(args) == len(func.graph.inputs), (args, func.graph.inputs)
#  Map inputs to function arguments.
for inp, arg in zip(func.graph.inputs, args):
    converter._add_conversion(inp, arg)
# Convert output tensors.
exit(tuple(
    [converter._convert_helper(x).t for x in func._func_graph_outputs]))
