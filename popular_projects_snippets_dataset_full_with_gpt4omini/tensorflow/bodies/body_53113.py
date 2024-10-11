# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=True):
        variable_node = variable_scope.get_variable(
            "variable_node", initializer=1.0)
        another_variable = variable_scope.get_variable(
            "unused_variable_node", initializer=2.0)
        with ops.control_dependencies(
            [variable_node.assign(another_variable + variable_node)]):
            output_node = array_ops.identity(variable_node, name="output_node")
        initializer_name = variable_node.initializer.name
        with session_lib.Session() as sess:
            self.evaluate(variable_node.initializer)
            self.evaluate(another_variable.initializer)
            output = self.evaluate(output_node)
            self.assertNear(3.0, output, 0.00001)
            variable_graph_def = sess.graph.as_graph_def()

            # Test variable name black list. This should result in the variable
            # not being a const.  Furthermore, the paths that read from and assign
            # to the denylisted variable should continue to be valid.
            constant_graph_def_with_denylist = (
                convert_to_constants
                .convert_variables_to_constants_from_session_graph(
                    session=sess,
                    graph_def=variable_graph_def,
                    output_node_names=["output_node", initializer_name],
                    variable_names_denylist=set(["variable_node"])))

            variable_node = None
            for node in constant_graph_def_with_denylist.node:
                if node.name == "variable_node":
                    variable_node = node
            self.assertIsNotNone(variable_node)
            self.assertEqual(variable_node.op, "VarHandleOp")

    # Now we make sure another_variable is now a constant, but the original
    # variable is not, and that the graph can be executed and update the
    # variable can be updated with each execution.
with ops.Graph().as_default():
    _ = importer.import_graph_def(constant_graph_def_with_denylist, name="")
    with session_lib.Session() as sess:
        output_node = sess.graph.get_tensor_by_name("output_node:0")
        self.evaluate(sess.graph.get_operation_by_name(initializer_name))
        output = self.evaluate(output_node)
        self.assertNear(3.0, output, 0.00001)
        output = self.evaluate(output_node)
        self.assertNear(5.0, output, 0.00001)
