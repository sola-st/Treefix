# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates `Operations` in this graph for any new TF_Operations.

    This is useful for when TF_Operations are indirectly created by the C API
    outside of the Operation constructor (e.g. by TF_ImportGraphDef,
    TF_FinishWhile). This ensures there are corresponding Operations for all
    TF_Operations in the underlying TF_Graph.

    Args:
      compute_devices: (Optional.) If True, device functions will be executed to
        compute the device properties of each new Operation.

    Returns:
      A list of the new `Operation` objects.
    """
self._check_not_finalized()

# Create all Operation objects before accessing their inputs since an op may
# be created before its inputs.
new_ops = [
    self._create_op_from_tf_operation(c_op, compute_device=compute_devices)
    for c_op in c_api_util.new_tf_operations(self)
]

# pylint: disable=protected-access
for op in new_ops:
    new_control_inputs = self._control_dependencies_for_inputs(op.inputs)
    op._add_control_inputs(new_control_inputs)
    op._control_flow_post_processing()
# pylint: enable=protected-access

exit(new_ops)
