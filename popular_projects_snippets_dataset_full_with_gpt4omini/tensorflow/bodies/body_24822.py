# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
rewriter_config = rewriter_config_pb2.RewriterConfig(
    dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    pin_to_host_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    min_graph_nodes=-1)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
exit(config_pb2.ConfigProto(graph_options=graph_options))
