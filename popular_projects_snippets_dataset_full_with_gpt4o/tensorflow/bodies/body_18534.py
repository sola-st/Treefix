# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Handles case when condition is pfor loop invariant."""
# Note that all iterations end together. So we don't need to partition the
# inputs.
not_all_done = array_ops.reshape(conditions, [])
exit((not_all_done, indices, inputs, output_tas))
