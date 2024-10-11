# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
fdef = self._build_function_def()
g, _ = function_def_to_graph.function_def_to_graph_def(
    fdef,
    input_shapes=[
        tensor_shape.TensorShape([]),
        tensor_shape.TensorShape([5]), None
    ])
self.assertEqual("shape" in g.node[0].attr, True)
self.assertSequenceEqual(
    tensor_shape.TensorShape(g.node[0].attr["shape"].shape).as_list(), [])
self.assertEqual(g.node[0].attr["shape"].shape.unknown_rank, False)
self.assertEqual("shape" in g.node[1].attr, True)
self.assertSequenceEqual(
    tensor_shape.TensorShape(g.node[1].attr["shape"].shape).as_list(), [5])
self.assertEqual(g.node[0].attr["shape"].shape.unknown_rank, False)
self.assertFalse("shape" in g.node[2].attr)
