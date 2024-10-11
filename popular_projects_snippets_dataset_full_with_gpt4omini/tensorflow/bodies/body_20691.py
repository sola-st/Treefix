# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Returns a ConfigProto with auto mixed precision enabled if appropriate."""
rewrite_config = rewriter_config_pb2.RewriterConfig(
    # do not remove duplicated nodes
    arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    # do not turn Conv2D and other nodes into _FusedConv2D
    remapping=rewriter_config_pb2.RewriterConfig.OFF,
)
if auto_mixed_precision_mode == 'cuda':
    rewrite_config.auto_mixed_precision = rewriter_config_pb2.RewriterConfig.ON
elif auto_mixed_precision_mode == 'mkl':
    rewrite_config.auto_mixed_precision_onednn_bfloat16 = (
        rewriter_config_pb2.RewriterConfig.ON)
else:
    assert auto_mixed_precision_mode is None
rewrite_config.min_graph_nodes = -1
graph_options = config_pb2.GraphOptions(
    rewrite_options=rewrite_config, build_cost_model=1)
config = config_pb2.ConfigProto(graph_options=graph_options)
config.graph_options.optimizer_options.opt_level = -1
exit(config)
