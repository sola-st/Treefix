# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Freezes a graph which contains a Switch with type RESOURCE_DT."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=True):
        x = variable_scope.get_variable("var_x", initializer=1.0)
        y = variable_scope.get_variable("var_y", initializer=2.0)
        f1 = lambda: variable_scope.get_variable("var_f1", initializer=17.0)
        f2 = lambda: variable_scope.get_variable("var_f2", initializer=23.0)
        cond_node = control_flow_ops.case([(gen_math_ops.less(x, y), f1)],
                                          default=f2)
        _ = math_ops.multiply(cond_node, 2.0, name="output_node")

        with session_lib.Session() as sess:
            sess.run(variables.global_variables_initializer())
            variable_graph_def = sess.graph.as_graph_def()

            constant_graph_def = (
                convert_to_constants
                .convert_variables_to_constants_from_session_graph(
                    session=sess,
                    graph_def=variable_graph_def,
                    output_node_names=["output_node"]))

self._ensure_no_variables_in_graph(constant_graph_def)
