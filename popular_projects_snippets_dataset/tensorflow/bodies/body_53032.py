# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two values using the message's CopyFrom/MergeFrom methods."""
merged = empty_fn()
merged.CopyFrom(x1)
merged.MergeFrom(x2)
exit(merged)
