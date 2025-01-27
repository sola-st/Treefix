# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py
test_cases = [{
    'shape': tensor_shape.TensorShape([])
}, {
    'shape': tensor_shape.TensorShape([3])
}, {
    'shape': tensor_shape.TensorShape([1, 2])
}, {
    'shape': tensor_shape.TensorShape([1, 2, 3])
}]

for test_case in test_cases:
    with ops.Graph().as_default() as g:
        iterator = iterator_ops.Iterator.from_structure(dtypes.int64)
        handle = iterator.string_handle()
        iterator = iterator_ops.Iterator.from_string_handle(
            handle, dtypes.int64, output_shapes=test_case['shape'])
        get_next = iterator.get_next()
        train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
        train_op.append(get_next)
        mg = meta_graph.create_meta_graph_def(graph=g)
        grappler_item = item.Item(mg)
        op_properties = grappler_item.GetOpProperties()
        self.assertEqual(test_case['shape'],
                         op_properties['IteratorGetNext'][0].shape)
