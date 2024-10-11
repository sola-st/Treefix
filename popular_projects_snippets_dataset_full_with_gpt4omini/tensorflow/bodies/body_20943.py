# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self.call_counter['after_run'] += 1
self.last_run_values = run_values
if self.should_stop:
    run_context.request_stop()
