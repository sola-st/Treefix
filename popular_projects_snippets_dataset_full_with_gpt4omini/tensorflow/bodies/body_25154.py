# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
rewriter_config = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=True,
    constant_folding=rewriter_config_pb2.RewriterConfig.OFF,
    arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    pin_to_host_optimization=rewriter_config_pb2.RewriterConfig.OFF)

graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
exit(config_pb2.ConfigProto(graph_options=graph_options))
