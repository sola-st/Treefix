# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item_test.py
with ops.Graph().as_default() as g:
    a = constant_op.constant(10)
    b = constant_op.constant(20)
    c = a + b
    z = control_flow_ops.no_op()
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(c)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)
    op_properties = grappler_item.GetOpProperties()

    # All the nodes in this model have one scalar output
    for node in grappler_item.metagraph.graph_def.node:
        node_prop = op_properties[node.name]

        if node.name == z.name:
            self.assertEqual(0, len(node_prop))
        else:
            self.assertEqual(1, len(node_prop))
            self.assertEqual(dtypes.int32, node_prop[0].dtype)
            self.assertEqual(tensor_shape.TensorShape([]), node_prop[0].shape)
