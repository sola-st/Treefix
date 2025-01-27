# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Helper to unpack a single tensor."""
if not isinstance(parallel_tensor, (
    ops.Tensor, composite_tensor.CompositeTensor, variables.Variable)):
    raise ValueError(
        "Expected a tensor, got {}.".format(parallel_tensor))
with ops.device(self._name):
    exit(tpu_ops.tpu_replicated_output(
        parallel_tensor, num_replicas=len(self.components)))
