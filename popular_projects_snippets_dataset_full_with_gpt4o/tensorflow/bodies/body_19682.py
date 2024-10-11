# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
"""Returns a variable handle for replicated TPU variable 'var'.

    This is a method used by an experimental replicated variable implementation
    and is not intended as a public API.

    Args:
      name: The common name of the variable.
      handle_id: Unique ID of the variable handle, used as the cache key.
      vars_: The replicated TPU variables or handles.
      is_mirrored: Whether the variables are mirrored, which guarantees the
        values in each replica are always the same.
      is_packed: Whether the replicated variables are packed into one variable.

    Returns:
      The handle of the TPU replicated input node.
    """
device_assignment = _enclosing_tpu_device_assignment()
# We don't need to put device assignment as part of the replicated_vars key
# because each TPUReplicateContext will only have one device assignment.
handle = self._replicated_vars.get(handle_id)
if handle is not None:
    exit(handle)

if device_assignment is not None and not is_packed:
    # Find a variable copy for each replica in the device assignment.
    # Note that the order of devices for replicas for the variable and the
    # device assignment might not match.
    job_name = pydev.DeviceSpec.from_string(vars_[0].device).job
    devices_to_vars = {device_util.canonicalize(v.device): v for v in vars_}
    replicated_vars = []
    for replica_id in range(device_assignment.num_replicas):
        for logical_core in range(device_assignment.num_cores_per_replica):
            device = device_util.canonicalize(
                device_assignment.tpu_device(
                    replica=replica_id, logical_core=logical_core, job=job_name))
            if device in devices_to_vars:
                replicated_vars.append(devices_to_vars[device])
                break
        else:
            raise ValueError(
                "Failed to find a variable on any device in replica {} for "
                "current device assignment".format(replica_id))
else:
    replicated_vars = vars_

# Builds a TPUReplicatedInput node for the variable, if one does not already
# exist. The TPUReplicatedInput node must belong to the enclosing
# control-flow scope of the TPUReplicateContext.
# TODO(phawkins): consider changing the contract of the TPU encapsulation
# so the TPUReplicatedInput nodes go inside the TPUReplicateContext scope
# instead.

_, graph = _enclosing_tpu_context_and_graph()
with graph.as_default():
    # If replicated_vars are variables, get the handles. Note that this can be
    # done inside TPUReplicateContext because replicated_vars.handle may
    # create new ops.
    if isinstance(replicated_vars[0], variables.Variable):
        replicated_vars = [v.handle for v in replicated_vars]
    # pylint: disable=protected-access
    saved_context = graph._get_control_flow_context()
    graph._set_control_flow_context(self.outer_context)
    handle = tpu_ops.tpu_replicated_input(
        replicated_vars,
        name=name + "/handle",
        is_mirrored_variable=is_mirrored,
        is_packed=is_packed)
    graph._set_control_flow_context(saved_context)
    # pylint: enable=protected-access
self._replicated_vars[handle_id] = handle
exit(handle)
