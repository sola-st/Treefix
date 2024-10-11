# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
"""Check that the swap annotations are followed."""
with ops.device('/gpu:0'):
    a = variables.VariableV1(10, name='a')
    b = variables.VariableV1(20, name='b')
    c = math_ops.add_n([a, b], name='c')
    d = math_ops.add_n([b, c], name='d')
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(d)

    d.op._set_attr('_swap_to_host', attr_value_pb2.AttrValue(i=0))

    mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())
    graph_size = len(mg.graph_def.node)

    config = config_pb2.ConfigProto()
    config.graph_options.rewrite_options.CopyFrom(
        rewriter_config_pb2.RewriterConfig(
            disable_model_pruning=True,
            meta_optimizer_iterations=rewriter_config_pb2.RewriterConfig.ONE,
            constant_folding=rewriter_config_pb2.RewriterConfig.OFF,
            memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL,
            min_graph_nodes=-1))
    graph = tf_optimizer.OptimizeGraph(config, mg)

    self.assertEqual(len(graph.node), graph_size + 2)
    self.assertTrue(
        set(node.name for node in graph.node) > set(
            ['a', 'b', 'c', 'd', 'swap_in_d_0', 'swap_out_d_0']))
    for node in graph.node:
        if node.name == 'swap_in_d_0':
            self.assertEqual('swap_out_d_0', node.input[0])
            self.assertEqual('^b/read', node.input[1])
        elif node.name == 'swap_out_d_0':
            self.assertEqual('b/read', node.input[0])
        elif node.name == 'd':
            self.assertEqual('swap_in_d_0', node.input[0])
            self.assertEqual('c', node.input[1])
