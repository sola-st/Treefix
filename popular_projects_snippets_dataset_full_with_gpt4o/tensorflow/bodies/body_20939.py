# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self.should_stop = False
self.request = None
self.call_counter = collections.Counter()
self.last_run_context = None
self.last_run_values = None
