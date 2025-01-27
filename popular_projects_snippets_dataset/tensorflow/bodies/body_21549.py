# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
"""Tests that gradients can be computed after exporting and importing.

    Builds a graph, exports it, and verifies that it can be imported and the
    gradient can be built and run correctly.

    Args:
      graph_fn: takes a single float Tensor argument as input, outputs a single
        Tensor
    """
test_dir = self._get_test_dir("nested_control_flow")
filename = os.path.join(test_dir, "metafile")
saver_ckpt = os.path.join(test_dir, "saver.ckpt")

# Create while loop using `outer_body_fn`.
with ops_lib.Graph().as_default():
    var = variables.VariableV1(0.0)
    var_name = var.name
    output = graph_fn(var)
    output_name = output.name
    init_op = variables.global_variables_initializer()

    # Generate a MetaGraphDef containing the while loop.
    with session.Session() as sess:
        self.evaluate(init_op)
        self.evaluate(output)
        saver = saver_module.Saver()
        saver.save(sess, saver_ckpt)
        saver.export_meta_graph(filename)

    # Build and run the gradients of the while loop. We use this below to
    # verify that the gradients are correct with an imported MetaGraphDef.
    grad = gradients_impl.gradients([output], [var])
    # Turn off constant folding to avoid breaking testNestedControlFlowSerDes.
    # It appears that a missing control dependency in the gradient graph
    # causes the fetch node to not be triggered.
    no_constfold_config = config_pb2.ConfigProto()
    no_constfold_config.graph_options.rewrite_options.constant_folding = (
        rewriter_config_pb2.RewriterConfig.OFF)
    with session.Session(config=no_constfold_config) as sess:
        self.evaluate(init_op)
        expected_grad_value = self.evaluate(grad)

    # Restore the MetaGraphDef into a new Graph.
with ops_lib.Graph().as_default():
    with session.Session() as sess:
        saver = saver_module.import_meta_graph(filename)
        saver.restore(sess, saver_ckpt)

    # Make sure we can still build gradients and get the same result.
    var = ops_lib.get_default_graph().get_tensor_by_name(var_name)
    output = ops_lib.get_default_graph().get_tensor_by_name(output_name)
    grad = gradients_impl.gradients([output], [var])

    init_op = variables.global_variables_initializer()

    with session.Session(config=no_constfold_config) as sess:
        self.evaluate(init_op)
        actual_grad_value = self.evaluate(grad)
        self.assertEqual(expected_grad_value, actual_grad_value)
