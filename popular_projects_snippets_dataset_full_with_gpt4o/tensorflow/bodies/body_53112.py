# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=use_resource):
        variable_node = variable_scope.get_variable(
            "variable_node", initializer=1.0)
        variable_scope.get_variable("unused_variable_node", initializer=1.0)
        output_node = math_ops.multiply(variable_node, 2.0, name="output_node")
        with session_lib.Session() as sess:
            self.evaluate(variable_node.initializer)
            output = self.evaluate(output_node)
            self.assertNear(2.0, output, 0.00001)
            variable_graph_def = sess.graph.as_graph_def()
            constant_graph_def = (
                convert_to_constants
                .convert_variables_to_constants_from_session_graph(
                    session=sess,
                    graph_def=variable_graph_def,
                    output_node_names=["output_node"]))

            self._ensure_no_variables_in_graph(constant_graph_def)

    # Now we make sure the variable is now a constant, and that the graph still
    # produces the expected result.
with ops.Graph().as_default():
    _ = importer.import_graph_def(constant_graph_def, name="")
    self.assertEqual(4, len(constant_graph_def.node))
    self._ensure_no_variables_in_graph(constant_graph_def)
    with session_lib.Session() as sess:
        output_node = sess.graph.get_tensor_by_name("output_node:0")
        output = self.evaluate(output_node)
        self.assertNear(2.0, output, 0.00001)
