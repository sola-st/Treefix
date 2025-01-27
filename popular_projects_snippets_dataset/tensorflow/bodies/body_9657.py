# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    self.assertProtoEquals('versions { producer: %d min_consumer: %d }' %
                           (versions.GRAPH_DEF_VERSION,
                            versions.GRAPH_DEF_VERSION_MIN_CONSUMER),
                           sess.graph_def)
    c = constant_op.constant(5.0, name='c')
    self.assertEqual(len(sess.graph_def.node), 1)
    d = constant_op.constant(6.0, name='d')
    self.assertEqual(len(sess.graph_def.node), 2)
    self.assertAllEqual(c, 5.0)
    self.assertAllEqual(d, 6.0)
    e = constant_op.constant(7.0, name='e')
    self.assertEqual(len(sess.graph_def.node), 3)
    self.assertAllEqual(e, 7.0)
