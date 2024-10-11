# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
ops.reset_default_graph()
self._server.clear_data()
self._server_2.clear_data()
super(SendTracebacksTest, self).tearDown()
