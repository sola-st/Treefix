# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/tf_optimizer_test.py
"""Make sure arguments can be passed correctly."""
a = constant_op.constant(10, name='a')
b = constant_op.constant(20, name='b')
c = math_ops.add_n([a, b], name='c')
d = math_ops.add_n([b, c], name='d')
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
# Being a train_op will make 'd' to be added as a fetch node.
train_op.append(d)
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())

config = config_pb2.ConfigProto()
rewriter_config = config.graph_options.rewrite_options
rewriter_config.optimizers.append('constfold')
rewriter_config.min_graph_nodes = -1

graph = tf_optimizer.OptimizeGraph(config, mg)

self.assertEqual(len(graph.node), 1)
self.assertItemsEqual([node.name for node in graph.node], ['d'])
