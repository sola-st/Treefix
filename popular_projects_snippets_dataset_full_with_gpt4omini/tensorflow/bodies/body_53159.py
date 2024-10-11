# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py

@function.Defun(dtypes.float32)
def F1(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

library = function_pb2.FunctionDefLibrary()
library.function.extend([F1.definition])

graph_def1 = graph_pb2.GraphDef()
graph_def1.library.CopyFrom(library)

graph_def2 = graph_pb2.GraphDef()
graph_def2.library.CopyFrom(library)

self.assertTrue(graph_util.graph_defs_equal(graph_def1, graph_def2))
