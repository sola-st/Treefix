# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution_digests = reader.executions(digest=True)
for i in range(99, 49, -1):
    execution = reader.read_execution(execution_digests[i])
    executions[i] = execution
