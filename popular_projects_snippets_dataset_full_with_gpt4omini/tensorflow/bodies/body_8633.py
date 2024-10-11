# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Helper to pack plain-old-tensors, not structures or composites."""
for tensor in tensors:
    if not isinstance(tensor, (ops.Tensor, composite_tensor.CompositeTensor,
                               variables.Variable)):
        raise ValueError(
            ("Every component to pack onto the ParallelDevice must already be "
             "a tensor, got {}. Consider running `tf.constant` or "
             "`tf.convert_to_tensor` first on literal values.")
            .format(tensors))
with ops.device(self._name):
    exit(tpu_ops.tpu_replicated_input(inputs=tensors))
