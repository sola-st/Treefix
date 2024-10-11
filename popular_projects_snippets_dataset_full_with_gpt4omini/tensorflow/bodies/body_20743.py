# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
rewrite_options = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=True,
    memory_optimization=rewriter_config_pb2.RewriterConfig.HEURISTICS)
graph_options = config_pb2.GraphOptions(rewrite_options=rewrite_options)
exit(config_pb2.ConfigProto(graph_options=graph_options))
