# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# pylint: disable=protected-access
self.assertIsNone(ops._default_session_stack.get_default())
# pylint: enable=protected-access
with ops.device('/cpu:0'):
    sess = session.Session()
    c_1 = constant_op.constant(5.0)
    with sess.graph.as_default():
        c_2 = constant_op.constant(5.0)
    self.assertEqual(c_1.graph, c_2.graph)
    self.assertEqual(sess.run(c_2), 5.0)
    with self.assertRaisesWithPredicateMatch(
        ValueError, lambda e: 'No default session is registered.' in str(e)):
        c_2.eval()
