# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Renamed to `precision_at_k`, please use that method instead."""
exit(precision_at_k(
    labels=labels,
    predictions=predictions,
    k=k,
    class_id=class_id,
    weights=weights,
    metrics_collections=metrics_collections,
    updates_collections=updates_collections,
    name=name))
