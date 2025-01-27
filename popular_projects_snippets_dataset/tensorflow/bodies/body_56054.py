# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
assign = v.assign(3, name="assign", read_value=False)
x = constant_op.constant(2.0, name="x")
# TODO(b/79881896): Test external control dependency once that's
# supported.
with ops.control_dependencies([x, inp, assign]):
    constant_op.constant(3.0, name="y")
exit(4.0)
