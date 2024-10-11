# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
rewriter_config = rewriter_config_pb2.RewriterConfig(
    pin_to_host_optimization=rewriter_config_pb2.RewriterConfig.OFF)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
exit(config_pb2.ConfigProto(graph_options=graph_options))
