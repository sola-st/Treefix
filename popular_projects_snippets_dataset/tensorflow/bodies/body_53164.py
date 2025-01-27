# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py

@function.Defun(dtypes.float32)
def F1(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

f1_def = F1.definition

library = function_pb2.FunctionDefLibrary()
library.function.extend([f1_def])

graph_def1 = graph_pb2.GraphDef()
graph_def1.library.CopyFrom(library)

reversed_function = function_pb2.FunctionDef()
reversed_function.CopyFrom(f1_def)
# Clear the node_def attribute.
del reversed_function.node_def[:]
reversed_function.node_def.extend(reversed(f1_def.node_def))
reversed_library = function_pb2.FunctionDefLibrary()
reversed_library.function.extend([reversed_function])
graph_def2 = graph_pb2.GraphDef()
graph_def2.library.CopyFrom(reversed_library)

self.assertTrue(graph_util.graph_defs_equal(graph_def1, graph_def2))
