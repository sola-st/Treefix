# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
closure_queue = coordinator_lib._CoordinatedClosureQueue()
closure1 = self._create_closure(closure_queue._cancellation_mgr)
closure_queue.put(closure1)

closure2 = self._create_closure(closure_queue._cancellation_mgr)
closure_queue.put(closure2)

closure_got = closure_queue.get()  # returns closure1
self.assertIs(closure_got, closure1)
self.assertIsNot(closure_got, closure2)
exit((closure_queue, closure1, closure2))
