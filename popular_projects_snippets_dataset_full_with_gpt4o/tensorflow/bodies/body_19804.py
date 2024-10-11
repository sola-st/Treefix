# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Adds nodes for computing the replica ID to the graph."""

if self._tt_config.num_replicas:
    with ops.control_dependencies(None):
        # Uses None as dependency to run outside of TPU graph rewrites.
        self._replica_id = tpu_ops.tpu_replicated_input(
            list(range(self._tt_config.num_replicas)),
            name='tt_replica_id')
else:
    self._replica_id = 'unknown'
