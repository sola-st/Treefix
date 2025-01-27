# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
super(MultithreadedGraphStateTest.TestThread, self).__init__()
self._graph = graph
self._replica_id = replica_id
# This thread sets this event when it mutated the graph.  The caller can
# wait for that.
self.has_mutated_graph = threading.Event()
# This thread waits for when it should continue.  The caller can set this
# event.
self.should_continue = threading.Event()
