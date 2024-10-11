# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""If this graph contains functions, copy them to `graph_def`."""
bytesize = starting_bytesize
for f in self._functions.values():
    bytesize += f.definition.ByteSize()
    if bytesize >= (1 << 31) or bytesize < 0:
        raise ValueError("GraphDef cannot be larger than 2GB.")
    graph_def.library.function.extend([f.definition])
    if f.grad_func_name:
        grad_def = function_pb2.GradientDef()
        grad_def.function_name = f.name
        grad_def.gradient_func = f.grad_func_name
        graph_def.library.gradient.extend([grad_def])
