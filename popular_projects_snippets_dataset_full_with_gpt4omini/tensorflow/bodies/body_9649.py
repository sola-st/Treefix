# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
ev.wait()
val = c.eval(session=sess)
self.assertEqual(val, 5.0)
