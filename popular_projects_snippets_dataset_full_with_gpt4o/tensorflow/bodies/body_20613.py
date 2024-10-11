# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py
with ops.Graph().as_default() as g:
    dataset = dataset_ops.Dataset.range(42)
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    get_next = iterator.get_next()
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(get_next)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)
    op_properties = grappler_item.GetOpProperties()
    self.assertEqual(
        tensor_shape.TensorShape([]),
        op_properties['IteratorGetNext'][0].shape)
