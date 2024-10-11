# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if layout_optimizer:
    rewrite_options = rewriter_config_pb2.RewriterConfig(
        layout_optimizer=rewriter_config_pb2.RewriterConfig.ON,
        # do not remove duplicated nodes
        arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF)
else:
    rewrite_options = rewriter_config_pb2.RewriterConfig(
        layout_optimizer=rewriter_config_pb2.RewriterConfig.OFF,
        # do not remove duplicated nodes
        arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF)
rewrite_options.min_graph_nodes = -1
graph_options = config_pb2.GraphOptions(
    rewrite_options=rewrite_options, build_cost_model=1)
config = config_pb2.ConfigProto(graph_options=graph_options)
config.graph_options.optimizer_options.opt_level = -1
exit(config)
