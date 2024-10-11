# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
"""Tests that rewriting occurs with non-standard gradient names."""
(original_metagraph, _, _, _) = self._GetMetaGraph(
    optimizer_scope_name='optimizer')
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.CopyFrom(
    rewriter_config_pb2.RewriterConfig(
        disable_model_pruning=True,
        constant_folding=rewriter_config_pb2.RewriterConfig.OFF,
        dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
        layout_optimizer=rewriter_config_pb2.RewriterConfig.OFF,
        arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
        min_graph_nodes=-1,
        memory_optimization=rewriter_config_pb2.RewriterConfig
        .RECOMPUTATION_HEURISTICS,
        # Checks that name scope "gradients/" also match sub-scope.
        memory_optimizer_target_node_name_scope='gradients/'))
rewritten_graph_def = tf_optimizer.OptimizeGraph(config, original_metagraph)
self.assertGreater(
    len(rewritten_graph_def.node),
    len(original_metagraph.graph_def.node))
self.assertEqual(
    0,
    len([node for node in original_metagraph.graph_def.node
         if 'Recomputed/' in node.name]))
self.assertEqual(
    20,  # Two per layer
    len([node for node in rewritten_graph_def.node
         if 'Recomputed/' in node.name]))
