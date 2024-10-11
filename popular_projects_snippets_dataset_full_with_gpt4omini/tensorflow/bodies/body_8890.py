# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
if sys.version_info >= (3, 8) and platform.system() == 'Windows':
    # TODO(b/165013260): Fix this
    self.skipTest('Test is currently broken on Windows with Python 3.8')

closure_queue, _, _ = self._put_two_closures_and_get_one()

self.assertFalse(closure_queue.done())
closure_queue.mark_failed(ValueError())
with self.assertRaises(ValueError):
    closure_queue.done()
