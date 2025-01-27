# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
queue = coordinator_lib._CoordinatedClosureQueue()

closure1 = self._create_closure(queue._cancellation_mgr)
closure2 = self._create_closure(queue._cancellation_mgr)
closure3 = self._create_closure(queue._cancellation_mgr)

def put_fn():
    queue.put(closure3, tag=1)
    queue.put(closure2, tag=2)
    queue.put(closure1)

def get_fn():
    # The get should only return the closure with tag 2.
    self.assertIs(closure2, queue.get(tag=2))

self._run_two_fns_in_parallel(put_fn, get_fn)

self.assertFalse(queue.done())
self.assertEqual(closure1, queue.get())
queue.mark_finished()

# It will not wait for closure3
self.assertTrue(queue.done())
queue.wait()
