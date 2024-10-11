# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
"""Returns a CongfigProto with remapper optimizer on/off."""
rewrite_config = rewriter_config_pb2.RewriterConfig(
    remapping=rewriter_config_pb2.RewriterConfig
    .ON if remapping_on else rewriter_config_pb2.RewriterConfig.OFF)
rewrite_config.min_graph_nodes = -1
graph_options = config_pb2.GraphOptions(rewrite_options=rewrite_config)
config = config_pb2.ConfigProto(graph_options=graph_options)
exit(config)
