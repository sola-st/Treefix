# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item_test.py
with ops.Graph().as_default() as g:
    a = constant_op.constant(10)
    b = constant_op.constant(20)
    c = a + b
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(c)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)
    op_list = grappler_item.IdentifyImportantOps()
    self.assertItemsEqual(['Const', 'Const_1', 'add'], op_list)
