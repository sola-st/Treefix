# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# It should not report the fake cancellation error.
with self.assertRaisesRegex(ValueError, 'Some error.'):
    # Verifying `wait()` or `put()` raises even if one closure is in
    # flight.
    if call_wait:
        closure_queue.wait()
    else:
        closure_queue.put(closure3)
