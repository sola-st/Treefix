# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
"""Make sure the graph is preserved when there is nothing to swap."""
a = variables.VariableV1(10, name='a')
b = variables.VariableV1(20, name='b')
c = math_ops.add_n([a, b], name='c')
d = math_ops.add_n([b, c], name='d')
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(d)
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())
graph_size = len(mg.graph_def.node)
nodes = [node.name for node in mg.graph_def.node]

config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.CopyFrom(
    rewriter_config_pb2.RewriterConfig(
        disable_model_pruning=True,
        constant_folding=rewriter_config_pb2.RewriterConfig.OFF,
        dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
        memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL))
graph = tf_optimizer.OptimizeGraph(config, mg)

self.assertEqual(len(graph.node), graph_size)
self.assertItemsEqual([node.name for node in graph.node], nodes)
