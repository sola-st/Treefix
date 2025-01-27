# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.CopyFrom(
    rewriter_config_pb2.RewriterConfig(
        constant_folding=rewriter_config_pb2.RewriterConfig.OFF,
        memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL))
exit(tf_optimizer.OptimizeGraph(config, mg))
