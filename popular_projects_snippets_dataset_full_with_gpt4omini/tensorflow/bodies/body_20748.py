# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
graph = self._annotated_graph()[0]
with graph.as_default():
    metagraph = train.export_meta_graph()
self.assertEqual(
    0,
    len([node for node in metagraph.graph_def.node
         if 'Recomputed/' in node.name]))
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.CopyFrom(
    rewriter_config_pb2.RewriterConfig(
        min_graph_nodes=-1,
        memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL))
rewritten_graph_def = tf_optimizer.OptimizeGraph(config, metagraph)
self.assertEqual(
    9,
    len([
        node for node in rewritten_graph_def.node
        if 'Recomputed/' in node.name
    ]))
