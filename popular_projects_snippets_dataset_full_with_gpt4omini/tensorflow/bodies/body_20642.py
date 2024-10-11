# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py
test_cases = [{
    'tensor': 0,
    'shape': tensor_shape.TensorShape([])
}, {
    'tensor': np.array([1, 2, 3]),
    'shape': tensor_shape.TensorShape([3])
}, {
    'tensor': np.array([[1, 2, 3]]),
    'shape': tensor_shape.TensorShape([3, 1])
}, {
    'tensor': np.array([[[1, 2, 3], [4, 5, 6]]]),
    'shape': tensor_shape.TensorShape([3, 2, 1])
}]

for test_case in test_cases:
    with ops.Graph().as_default() as g:
        dataset = dataset_ops.Dataset.from_tensors(test_case['tensor'])
        dataset = dataset.map(array_ops.transpose)
        iterator = dataset_ops.make_one_shot_iterator(dataset)
        get_next = iterator.get_next()
        train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
        train_op.append(get_next)
        mg = meta_graph.create_meta_graph_def(graph=g)
        grappler_item = item.Item(mg)
        op_properties = grappler_item.GetOpProperties()
        self.assertEqual(test_case['shape'],
                         op_properties['IteratorGetNext'][0].shape)
