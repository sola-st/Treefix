# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
f = lambda distribution, value: distribution.extended.read_var(value)
exit(_aggregate_across_replicas(collections, f, v))
