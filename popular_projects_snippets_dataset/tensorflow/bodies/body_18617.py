# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
# Override to suppress ResourceSummaryWriter implementation; we don't need
# the deleter since TrackableResource.__del__() handles it for us.
pass
