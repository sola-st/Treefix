# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
if sys.version_info >= (3, 8) and platform.system() == 'Windows':
    # TODO(b/165013260): Fix this
    self.skipTest('Test is currently broken on Windows with Python 3.8')

closure_queue = coordinator_lib._CoordinatedClosureQueue()
closure_queue.put(self._create_closure(closure_queue._cancellation_mgr))
closure = closure_queue.get()

wait_finish_event = threading.Event()
coord = coordinator.Coordinator(clean_stop_exception_types=[])

# Using a thread to verify that closure_queue.wait() will not return until
# all inflight closures are finished.

def mark_finished_fn():
    try:
        raise ValueError('Some error.')
    except ValueError as e:
        closure_queue.mark_failed(e)

def wait_fn():
    with self.assertRaises(ValueError):
        closure_queue.wait()

self._assert_one_unblock_the_other(mark_finished_fn, wait_fn)

self.assertTrue(closure_queue.done())
