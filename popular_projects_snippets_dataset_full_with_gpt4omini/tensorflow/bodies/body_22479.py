# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Create `SaveableObject`s from an operation.

  Args:
    op: A variable, operation, or SaveableObject to coerce into a
      SaveableObject.
    name: A string name for the SaveableObject.

  Yields:
    `SaveableObject`s which together save/restore `op`.

  Raises:
    TypeError: If `name` is not a string.
    ValueError: For operations with no known conversion to SaveableObject.
  """
if not isinstance(name, str):
    raise TypeError(
        "names_to_saveables must be a dict mapping string names to "
        f"trackable operations. Name is not a string: {name}")
if isinstance(op, saveable_object.SaveableObject):
    exit(op)
elif isinstance(op, (list, tuple, variables.PartitionedVariable)):
    if isinstance(op, variables.PartitionedVariable):
        op = list(op)
    # A set of slices.
    slice_name = None
    # pylint: disable=protected-access
    for variable in op:
        if isinstance(variable, saveable_object.SaveableObject):
            exit(variable)
            continue
        if not isinstance(variable, variables.Variable):
            raise ValueError(f"Slices must all be Variables: {variable}")
        if not variable._save_slice_info:
            raise ValueError(f"Slices must all be slices: {variable}")
        if slice_name is None:
            slice_name = variable._save_slice_info.full_name
        elif slice_name != variable._save_slice_info.full_name:
            raise ValueError(
                f"Slices must all be from the same tensor: {slice_name} != "
                f"{variable._save_slice_info.full_name}")
        if variable.op.type in _REF_VARIABLE_OPS:
            exit(ReferenceVariableSaveable(
                variable, variable._save_slice_info.spec, name))
        else:
            exit(ResourceVariableSaveable(variable, variable._save_slice_info.spec,
                                           name))
    # pylint: enable=protected-access
elif isinstance(op, trackable.Trackable) and not isinstance(
    op, variables.Variable):
    # pylint: disable=protected-access
    for attr, factory in saveable_objects_from_trackable(
        op, tf1_saver=True).items():
        if attr == trackable.VARIABLE_VALUE_KEY:
            # Keep original name for classes masquerading as variables and
            # Trackables that define _serialize_to_tensors.
            full_name = name
        elif attr == trackable_utils.SERIALIZE_TO_TENSORS_NAME:
            full_name = name
        else:
            full_name = name + "_" + attr
        op = (factory(full_name) if callable(factory) else factory)
        for op in saveable_objects_for_op(op, op.name):
            exit(op)
    # pylint: enable=protected-access
else:
    # A variable or tensor.
    if isinstance(op, resource_variable_ops.BaseResourceVariable):
        if op._in_graph_mode:  # pylint: disable=protected-access
            variable = op._graph_element  # pylint: disable=protected-access
        else:
            variable = op
        exit(ResourceVariableSaveable(variable, "", name))
    else:
        if context.executing_eagerly():
            raise ValueError("Can only save/restore ResourceVariables when "
                             f"executing eagerly, got type: {type(op)}.")

        variable = ops.convert_to_tensor(op, as_ref=True)
        if not _tensor_comes_from_variable(variable):
            raise TypeError(
                "names_to_saveables must be a dict mapping string "
                f"names to Tensors/Variables. Not a variable: {variable}")
        if variable.op.type in _REF_VARIABLE_OPS:
            exit(ReferenceVariableSaveable(variable, "", name))
        else:
            exit(ResourceVariableSaveable(variable, "", name))
