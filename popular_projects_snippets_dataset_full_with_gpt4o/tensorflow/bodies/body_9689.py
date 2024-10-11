# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
config_pb = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(infer_shapes=True))
with ops.Graph().as_default(), ops.device('/cpu:0'):
    a = constant_op.constant([[1, 2]])
    sess = session.Session(config=config_pb)
    self.assertIn('_output_shapes', sess.graph_def.node[0].attr)
    # Avoid lint error regarding 'unused' var a.
    self.assertEqual(a, a)
