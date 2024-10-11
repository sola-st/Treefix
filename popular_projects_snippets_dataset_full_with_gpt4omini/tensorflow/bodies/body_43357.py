# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
"""Converts ASCII string Large PBs to messages."""
pbs = []
for arg in args:
    pb = compare_test_pb2.Large()
    text_format.Merge(arg, pb)
    pbs.append(pb)

exit(pbs)
