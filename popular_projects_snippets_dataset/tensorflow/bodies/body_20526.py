# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
with ops.Graph().as_default():
    a = array_ops.placeholder(dtype=dtypes.float32, name="a")
    b = array_ops.placeholder(dtype=dtypes.float32, name="b")
    constant_op.constant(1.0, name="constant")
    x = variable_scope.get_variable(
        name="x",
        dtype=dtypes.float32,
        shape=[],
        use_resource=True,
        initializer=init_ops.constant_initializer(2.0))
    y = variable_scope.get_variable(
        name="y",
        dtype=dtypes.float32,
        shape=[],
        use_resource=True,
        initializer=init_ops.constant_initializer(3.0))
    math_ops.add(a, b)
    math_ops.add(x, y)
    graph_def = ops.get_default_graph().as_graph_def()

    for node in graph_def.node:
        # Attach a TPU_REPLICATE_ATTR to each node.
        node.attr[tpu._TPU_REPLICATE_ATTR].s = b"0"
        # Rewire placeholder "a" and variable "y" leaving them unconnected.
        for (input_index, node_input) in enumerate(node.input):
            if node_input == "b":
                node.input[input_index] = "constant"
            if node_input == "y":
                node.input[input_index] = "x"

with ops.Graph().as_default() as graph:
    # Reimport the graph and prune unconnected ops.
    importer.import_graph_def(graph_def)
    tpu.prune_unconnected_ops_from_xla(ops.get_default_graph())

    # Verify that ops "a" and "x" still have TPU_REPLICATE_ATTR.
    a = graph.get_operation_by_name("import/a").get_attr(
        tpu._TPU_REPLICATE_ATTR)
    self.assertEqual(b"0", a)
    x = graph.get_operation_by_name("import/x").get_attr(
        tpu._TPU_REPLICATE_ATTR)
    self.assertEqual(b"0", x)
    # Verify that ops "b" and "y" have TPU_REPLICATE_ATTR removed.
    with self.assertRaisesRegex(
        ValueError,
        "Operation \'import/b\' has no attr named \'_tpu_replicate\'"):
        graph.get_operation_by_name("import/b").get_attr(
            tpu._TPU_REPLICATE_ATTR)
    with self.assertRaisesRegex(
        ValueError,
        "Operation \'import/y\' has no attr named \'_tpu_replicate\'"):
        graph.get_operation_by_name("import/y").get_attr(
            tpu._TPU_REPLICATE_ATTR)
