# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
meta_graph = _simple_metagraph()
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.CopyFrom(
    rewriter_config_pb2.RewriterConfig(
        layout_optimizer=rewriter_config_pb2.RewriterConfig.ON,
        min_graph_nodes=-1))
optimized_graph = tf_optimizer.OptimizeGraph(
    config, meta_graph, cluster=_get_cluster())

found = 0
for node in optimized_graph.node:
    if node.op in ['Conv2D', 'Conv2DBackpropFilter', 'Conv2DBackpropInput']:
        found += 1
        self.assertEqual(node.attr['data_format'].s, b'NCHW')
self.assertEqual(found, 5)
