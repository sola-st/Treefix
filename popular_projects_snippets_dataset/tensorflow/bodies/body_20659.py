# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/tf_optimizer_test.py
g = ops.Graph()
with g.as_default():
    a1 = variables.VariableV1(
        1.0)  # Must be preserved since it's in the collection 'variables'.
    a2 = constant_op.constant(0, shape=[50, 50], name='keep')
    ops.add_to_collection('a2', a2)  # Explicitly add to collection.
    with g._attr_scope(
        {'_grappler_do_not_remove': attr_value_pb2.AttrValue(b=True)}):
        a3 = constant_op.constant(0, name='keep2')
    b = constant_op.constant(1, shape=[100, 10])
    c = constant_op.constant(0, shape=[10, 30])
    d = math_ops.matmul(b, c)
    ops.add_to_collection('train_op', d)  # d is the fetch node.

# Optimize the graph.
mg = meta_graph.create_meta_graph_def(graph=g)
config = config_pb2.ConfigProto()
rewriter_config = config.graph_options.rewrite_options
rewriter_config.min_graph_nodes = -1
optimized_graph = tf_optimizer.OptimizeGraph(config, mg)

# Check that the nodes referenced in various collections have been preserved
optimized_graph_nodes = [node.name for node in optimized_graph.node]
expected_nodes = [
    d.op.name, a1.op.name, a2.op.name, a3.op.name, 'Variable/initial_value',
    'Variable/Assign'
]
self.assertEqual(len(optimized_graph_nodes), len(expected_nodes))
self.assertAllInSet(optimized_graph_nodes, expected_nodes)
