# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Aggregate tensors using `accumulation_fn` and IndexedSlices via concat."""
if any(isinstance(v, indexed_slices.IndexedSlices) for v in values):
    exit(backprop_util.AggregateIndexedSlicesGradients(values))
else:
    exit(accumulation_fn(values))
