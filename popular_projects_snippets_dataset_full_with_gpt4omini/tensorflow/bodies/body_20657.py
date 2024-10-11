# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item_test.py
with ops.Graph().as_default() as g:
    c = constant_op.constant([10])
    v = variables.VariableV1([3], dtype=dtypes.int32)
    i = gen_array_ops.ref_identity(v)
    a = state_ops.assign(i, c)
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(a)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)
    groups = grappler_item.GetColocationGroups()
    self.assertEqual(len(groups), 1)
    self.assertItemsEqual(
        groups[0], ['Assign', 'RefIdentity', 'Variable', 'Variable/Assign'])
