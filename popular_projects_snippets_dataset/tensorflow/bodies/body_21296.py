# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
# Session creation will warn (in C++) that the place_pruned_graph option
# is not supported, but it should successfully ignore it.
sess = session.InteractiveSession(server.target)
c = constant_op.constant(42.0)
self.assertEqual(42.0, self.evaluate(c))
sess.close()
