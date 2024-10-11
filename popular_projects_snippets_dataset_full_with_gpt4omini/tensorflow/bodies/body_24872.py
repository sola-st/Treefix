# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution_digests = reader.executions(digest=True)
# Read in the reverse order to enhance randomness of the read access.
for i in range(49, -1, -1):
    execution = reader.read_execution(execution_digests[i])
    executions[i] = execution
