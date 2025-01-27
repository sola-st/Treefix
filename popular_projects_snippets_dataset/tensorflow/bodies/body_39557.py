# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Copy the checkpointed variables from the accelerator to the host CPU.

    TODO(chienchunh): Get the concrete function before firstly called to avoid
                      hangining the accelerators idle during function tracing.
    """
for accelerator_var, cpu_var in self._object_map.items():
    if isinstance(accelerator_var, (ShardedVariable, TPUEmbedding)):
        # Skip for SharededVariable and TPUEmbedding as their sub-variables will
        # be copied over separately through other entries in the object map.
        continue
    with ops.device(cpu_var.device):
        cpu_var.assign(accelerator_var.read_value())
for tpu_embedding in self._tpu_embedding_objects:
    tpu_embedding._retrieve_variables()  # pylint: disable=protected-access
