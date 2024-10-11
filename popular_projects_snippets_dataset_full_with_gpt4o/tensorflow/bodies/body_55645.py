# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
# Create a simple while loop.
with ops.Graph().as_default():
    with ops.name_scope("export"):
        var = variables.Variable(0.)
        var_name = var.name
        _, output = control_flow_ops.while_loop(
            lambda i, x: i < 5,
            lambda i, x: (i + 1, x + math_ops.cast(i, dtypes.float32)),
            [0, var])
        output_name = output.name

    # Generate a MetaGraphDef containing the while loop with an export scope.
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        export_scope="export")

    # Build and run the gradients of the while loop. We use this below to
    # verify that the gradients are correct with the imported MetaGraphDef.
    init_op = variables.global_variables_initializer()
    grad = gradients_impl.gradients([output], [var])
    with session.Session() as sess:
        self.evaluate(init_op)
        expected_grad_value = self.evaluate(grad)

    # Restore the MetaGraphDef into a new Graph with an import scope.
with ops.Graph().as_default():
    meta_graph.import_scoped_meta_graph(meta_graph_def, import_scope="import")

    # Re-export and make sure we get the same MetaGraphDef.
    new_meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        export_scope="import")
    test_util.assert_meta_graph_protos_equal(
        self, meta_graph_def, new_meta_graph_def)

    # Make sure we can still build gradients and get the same result.

    def new_name(tensor_name):
        base_tensor_name = tensor_name.replace("export/", "")
        exit("import/" + base_tensor_name)

    var = ops.get_default_graph().get_tensor_by_name(new_name(var_name))
    output = ops.get_default_graph().get_tensor_by_name(new_name(output_name))
    grad = gradients_impl.gradients([output], [var])

    init_op = variables.global_variables_initializer()

    with session.Session() as sess:
        self.evaluate(init_op)
        actual_grad_value = self.evaluate(grad)
        self.assertEqual(expected_grad_value, actual_grad_value)
