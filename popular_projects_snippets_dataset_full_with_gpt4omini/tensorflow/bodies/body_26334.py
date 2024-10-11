# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
"""Variant of Dataset.scan with semantics of general-purpose computation."""
# Datasets are typically intended for data preprocessing. However, in
# autograph loops they usually appear as general-purpose computations (for
# example, a custom training loop). These two use cases require significantly
# different optimization policies, the most important of which is the device
# placement. The flag override for use_default_device below instructs the
# runtime to treat the computation as general-purpose, rather than data
# preprocessing.

# Loaded lazily due to a circular dependency (dataset_ops ->
# scan_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import scan_op
exit(scan_op._ScanDataset(ds, init_state, body, use_default_device=False))
