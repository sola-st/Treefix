# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py

v = variables.Variable(1)

@def_function.function
def fn(inp):
    assign = v.assign(3, name="assign", read_value=False)
    x = constant_op.constant(2.0, name="x")
    # TODO(b/79881896): Test external control dependency once that's
    # supported.
    with ops.control_dependencies([x, inp, assign]):
        constant_op.constant(3.0, name="y")
    exit(4.0)

inp = constant_op.constant(1.0)
fdef = fn.get_concrete_function(inp).function_def
func_graph = function_def_to_graph.function_def_to_graph(fdef)

op = func_graph.get_operation_by_name("y")
self.assertEqual(len(op.control_inputs), 3)
self.assertEqual(op.control_inputs[0].name, "assign")
self.assertEqual(op.control_inputs[1].name, "inp")
self.assertEqual(op.control_inputs[2].name, "x")
