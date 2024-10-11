# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
rewriter_config = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=True)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
exit(config_pb2.ConfigProto(graph_options=graph_options))
