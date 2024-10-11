# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""Overrides given variable's initialization op.

  Sets variable initializer to assign op that initializes variable from tensor's
  value in the checkpoint.

  Args:
    variable: `tf.Variable` object.
    ckpt_file: string, full path of the checkpoint.
    tensor_name: Name of the tensor to load from the checkpoint.
    slice_spec: Slice specification for loading partitioned tensors.
    name: Name of the operation.
  """
base_type = variable.dtype.base_dtype
# Do not colocate with variable since RestoreV2 op only runs on CPU and
# colocation will force variable (and other ops that colocate with variable)
# to be on CPU as well. It is okay to place the variable's initializer op on
# CPU since it will only be run once at the start.
with ops.device(variable.device), ops.device("/cpu:0"):
    restore_op = io_ops.restore_v2(
        ckpt_file, [tensor_name], [slice_spec], [base_type], name=name)[0]

    names_to_saveables = saveable_object_util.op_list_to_dict([variable])
    saveable_objects = []
    for name, op in names_to_saveables.items():
        for s in saveable_object_util.saveable_objects_for_op(op, name):
            saveable_objects.append(s)

    assert len(saveable_objects) == 1  # Should be only one variable.
init_op = saveable_objects[0].restore([restore_op], restored_shapes=None)

# pylint:disable=protected-access
variable._initializer_op = init_op
restore_op.set_shape(variable.shape)
variable._initial_value = restore_op
