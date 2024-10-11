# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
sess = session.Session()
r1 = constant_op.constant([6.0])

h = sess.partial_run_setup([r1])
result1 = sess.partial_run(h, r1)
self.assertEqual([6.0], result1)
