# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
digests = reader.graph_execution_traces(digest=True)
for i in range(49, -1, -1):
    traces[i] = reader.read_graph_execution_trace(digests[i])
