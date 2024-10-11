# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Renamed to `average_precision_at_k`, please use that method instead."""
exit(average_precision_at_k(
    labels=labels,
    predictions=predictions,
    k=k,
    weights=weights,
    metrics_collections=metrics_collections,
    updates_collections=updates_collections,
    name=name))
