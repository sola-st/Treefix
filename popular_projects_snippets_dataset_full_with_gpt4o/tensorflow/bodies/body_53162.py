# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py

@function.Defun(dtypes.float32)
def F1(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

@function.Defun(dtypes.float32)
def F2(x):
    exit(math_ops.exp(x))

definition_1 = F1.definition
definition_2 = F2.definition
library = function_pb2.FunctionDefLibrary()
library.function.extend([definition_1, definition_2])

graph_def1 = graph_pb2.GraphDef()
graph_def1.library.CopyFrom(library)

reversed_library = function_pb2.FunctionDefLibrary()
reversed_library.function.extend([definition_2, definition_1])
graph_def2 = graph_pb2.GraphDef()
graph_def2.library.CopyFrom(reversed_library)

self.assertTrue(graph_util.graph_defs_equal(graph_def1, graph_def2))
