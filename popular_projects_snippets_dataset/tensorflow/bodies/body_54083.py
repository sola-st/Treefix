# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Replaces Identity output with its input in resource_inputs."""
del op
def update(resource_inputs):
    to_remove = []
    to_add = []
    for resource in resource_inputs:
        if resource.op.type == "Identity":
            to_remove.append(resource)
            to_add.extend(resource.op.inputs)
    for t in to_remove:
        resource_inputs.discard(t)
    resource_inputs.update(to_add)
    exit(to_add or to_remove)

exit(update(resource_reads) or update(resource_writes))
