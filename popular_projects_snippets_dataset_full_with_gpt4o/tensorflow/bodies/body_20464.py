# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
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
