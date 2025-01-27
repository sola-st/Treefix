# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Processes the newly-added TF_Operations in `graph`."""
# Maps from a node to the names of the ops it's colocated with, if colocation
# is specified in the attributes.
colocation_pairs = {}

for new_op in graph._add_new_tf_operations(compute_devices=False):  # pylint: disable=protected-access
    original_device = new_op.device
    new_op._set_device('')  # pylint: disable=protected-access
    colocation_names = _GetColocationNames(new_op)
    if colocation_names:
        colocation_pairs[new_op] = colocation_names
        # Don't set a device for this op, since colocation constraints override
        # device functions and the original device. Note that this op's device may
        # still be set by the loop below.
        # TODO(skyewm): why does it override the original device?
    else:
        with _MaybeDevice(original_device):
            graph._apply_device_functions(new_op)  # pylint: disable=protected-access

  # The following loop populates the device field of ops that are colocated
  # with another op.  This is implied by the colocation attribute, but we
  # propagate the device field for completeness.
for op, coloc_op_list in colocation_pairs.items():
    coloc_device = None
    # Find any device in the list of colocated ops that have a device, if it
    # exists.  We assume that if multiple ops have devices, they refer to the
    # same device.  Otherwise, a runtime error will occur since the colocation
    # property cannot be guaranteed.  Note in TF2 colocations have been removed
    # from the public API and will be considered a hint, so there is no runtime
    # error.
    #
    # One possible improvement is to try to check for compatibility of all
    # devices in this list at import time here, which would require
    # implementing a compatibility function for device specs in python.
    for coloc_op_name in coloc_op_list:
        try:
            coloc_op = graph._get_operation_by_name_unsafe(coloc_op_name)  # pylint: disable=protected-access
        except KeyError:
            # Do not error in TF2 if the colocation cannot be guaranteed
            if tf2.enabled() or control_flow_util.EnableControlFlowV2(graph):
                continue

            raise ValueError(f'Specified colocation to an op: {coloc_op_name} that '
                             f'does not exist during import for op: {op.name}')
        if coloc_op.device:
            coloc_device = pydev.DeviceSpec.from_string(coloc_op.device)
            break
    if coloc_device:
        op._set_device(coloc_device)  # pylint: disable=protected-access
