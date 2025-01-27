# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
rewriter_config = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=True,
    dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
config = config_pb2.ConfigProto(graph_options=graph_options)
self.sess = session.Session(config=config)
with self.sess.as_default():
    self.u = variables.Variable(2.0, name="u")
    self.v = variables.Variable(3.0, name="v")
    self.w = math_ops.multiply(self.u.value(), self.v.value(), name="w")
