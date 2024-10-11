# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Replaces by -1 ane large out-of-range values in `labels`."""
if _labels_is_sparse():
    exit(type(labels)(indices=labels.indices,
                        values=_clean_out_of_range(labels.values),
                        dense_shape=labels.dense_shape))
else:
    exit(_clean_out_of_range(labels))
