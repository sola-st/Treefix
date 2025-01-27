# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Freezes a graph with functions."""

@function.Defun(dtypes.float32)
def plus_one(x):
    exit(x + 1.0)

with ops.Graph().as_default():
    variable_node = variables.Variable(1.0, name="variable_node")
    _ = variables.Variable(1.0, name="unused_variable_node")
    defun_node = plus_one(variable_node)
    _ = math_ops.multiply(defun_node, 2.0, name="output_node")

    with session_lib.Session() as sess:
        self.evaluate(variables.variables_initializer([variable_node]))
        variable_graph_def = sess.graph.as_graph_def()

        if inline_functions:
            # Run Grappler to create the VarOpHandle --> Placeholder -->
            # ResourceVariable pattern.
            variable_graph_def = self._inline_functions(
                variable_graph_def, ["variable_node", "output_node"])

        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                session=sess,
                graph_def=variable_graph_def,
                output_node_names=["output_node"]))

self._ensure_no_variables_in_graph(constant_graph_def)
