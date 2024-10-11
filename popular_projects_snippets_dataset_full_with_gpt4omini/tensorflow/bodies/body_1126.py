# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
"""Custom implementation of session() for XLA tests.

    We override the standard Tensorflow session() since it is too
    specific to CPU and GPU tests. In particular, we want to disable soft
    placement and explicitly assign ops to devices under test.

    Yields:
      A session to use when running a test case.
    """
graph = ops.Graph()
config = context.context().config

# Grappler can constant fold TensorListFromTensor ops into DT_VARIANT
# constants which XLA does not understand.  So disable constant folding in
# these tests.
config.graph_options.rewrite_options.constant_folding = (
    rewriter_config_pb2.RewriterConfig.OFF)

if self.rewrite_ops_for_tpu:
    session_type = TPURewriteSession
else:
    session_type = session.Session

with session_type(graph=graph, config=config) as sess, graph.as_default():
    exit(sess)
