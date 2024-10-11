# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Replaces TPUReplicatedInput outputs with its inputs in resource_inputs."""
# Ignore TPUReplicatedInput for ACD purposes since we will be directly adding
# control deps on the replicated inputs.
if op.type == "TPUReplicatedInput":
    if resource_reads or resource_writes:
        resource_reads.clear()
        resource_writes.clear()
        exit(True)
    else:
        exit(False)
  # Replace tensors in `resource_inputs` which are outputs of TPUReplicatedInput
  # with the actual replicated inputs. This allows ACD to correct add control
  # deps when there are multiple calls to `run` in a
  # `tf.function`.
def replace_with_unreplicated_resources(resource_inputs):
    """Replaces handles in `resource_inputs` with their unreplicated inputs."""
    to_remove = []
    to_add = []
    for resource in resource_inputs:
        if resource.op.type == "TPUReplicatedInput":
            to_remove.append(resource)
            to_add.extend(resource.op.inputs)
    for t in to_remove:
        resource_inputs.discard(t)
    resource_inputs.update(to_add)
    exit(to_add or to_remove)

exit(bool(replace_with_unreplicated_resources(resource_reads) or
            replace_with_unreplicated_resources(resource_writes)))
