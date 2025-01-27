# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# Read in the reverse order to enhance randomness of the read access.
for i in range(49, -1, -1):
    lines[i] = reader.source_lines("localhost", "/tmp/file_%d.py" % i)
