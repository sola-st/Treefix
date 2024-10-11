# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_grappler_test.py
"""Constructs a Session config proto that explicitly enables Grappler.

  Returns:
    A config proto that obtains extra safety for the unit tests in this
    file by ensuring that the relevant Grappler rewrites are always enabled.
  """
rewriter_config = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=False,
    arithmetic_optimization=rewriter_config_pb2.RewriterConfig.ON)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
exit(config_pb2.ConfigProto(graph_options=graph_options))
