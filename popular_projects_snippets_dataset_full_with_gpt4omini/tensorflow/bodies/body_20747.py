# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
# Closer to expected usage, but does not check that a re-write actually
# happens; see testHintDoesRewrite.
graph, init_op, train_op = self._annotated_graph()
with graph.as_default():
    manual_memory_config = rewriter_config_pb2.RewriterConfig(
        memory_optimization=rewriter_config_pb2.RewriterConfig.MANUAL)
    graph_options = config_pb2.GraphOptions(
        rewrite_options=manual_memory_config)
    session_config = config_pb2.ConfigProto(graph_options=graph_options)
    with session.Session(config=session_config) as sess:
        self.evaluate(init_op)
        self.evaluate(train_op)
