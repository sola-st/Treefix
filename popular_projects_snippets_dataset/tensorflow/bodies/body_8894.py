# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
if sys.version_info >= (3, 8) and platform.system() == 'Windows':
    # TODO(b/165013260): Fix this
    self.skipTest('Test is currently broken on Windows with Python 3.8')

closure_queue, closure1, closure2 = self._put_two_closures_and_get_one()
closure_queue.put(self._create_closure(closure_queue._cancellation_mgr))
closure_queue.get()
# At this moment, there are two inflight, one in queue.
self.assertEqual(closure_queue._inflight_closure_count, 2)

# Hold a copy of the queue's cancellation manager at this point
initial_cm = closure_queue._cancellation_mgr

# Simulating closure1 fails.
self._set_error(closure_queue, closure1, ValueError('Some error.'))

# At this moment, there are one inflight, one in queue.
self.assertEqual(closure_queue._queue.qsize(), 1)
self.assertEqual(closure_queue._inflight_closure_count, 1)

closure3 = self._create_closure(closure_queue._cancellation_mgr)

def fake_cancellation():
    self._set_error(closure_queue, closure2,
                    ValueError('Fake cancellation error.'))

def report_error():
    # It should not report the fake cancellation error.
    with self.assertRaisesRegex(ValueError, 'Some error.'):
        # Verifying `wait()` or `put()` raises even if one closure is in
        # flight.
        if call_wait:
            closure_queue.wait()
        else:
            closure_queue.put(closure3)

self._assert_one_unblock_the_other(fake_cancellation, report_error)

# The original cancellation manager of the queue has been cancelled.
self.assertTrue(initial_cm.is_cancelled)

# At this moment, there is zero inflight, nothing in queue.
self.assertTrue(closure_queue._queue.empty())
self.assertEqual(closure_queue._inflight_closure_count, 0)
self.assertIsNone(closure_queue._error)

# This asserts that closure1 has errored.
with self.assertRaisesRegex(ValueError, 'Some error.'):
    closure1.output_remote_value.fetch()

# The following asserts that closure3 should have been cancelled.
if not call_wait:
    with self.assertRaisesRegex(
        errors.CancelledError,
        'The corresponding function is cancelled. Please reschedule the '
        'function.'):
        closure3.output_remote_value.fetch()

    # Closure2 was an inflight closure when it got cancelled.
self.assertEqual(closure2.output_remote_value._status,
                 values_lib.RemoteValueStatus.READY)
with self.assertRaisesRegex(ValueError, 'Fake cancellation error.'):
    closure2.output_remote_value.fetch()

# This asserts that the queue has a clear state.
self.testBasic()
