# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
if execution_index in self.executions:
    raise ValueError("Duplicate execution index: %d" % execution_index)
self.executions[execution_index] = execution
