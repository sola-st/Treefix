# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py

@def_function.function
def fn(x):
    exit(x)

inp = constant_op.constant(1.0)
fdef = fn.get_concrete_function(inp).function_def
fdef.arg_attr[0].attr["_test_attr"].s = "value".encode("ascii")
graph_def = function_def_to_graph.function_def_to_graph_def(fdef)
placeholders = [
    ndef for ndef in graph_def[0].node if ndef.op == "Placeholder"
]
self.assertEqual(1, len(placeholders))
self.assertEqual(placeholders[0].attr["_test_attr"].s,
                 "value".encode("ascii"))
