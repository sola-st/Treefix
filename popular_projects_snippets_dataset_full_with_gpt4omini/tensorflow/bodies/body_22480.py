# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Create a dictionary of names to operation lists.

  This method is only used when the variable name matters (e.g. when saving
  or restoring from a TF1 name-based checkpoint). In TF2, this can be called
  from `tf.train.Checkpoint.restore` when loading from a name-based checkpoint.

  Args:
    op_list: A (nested) list, tuple, or set of Variables or SaveableObjects.
    convert_variable_to_tensor: Whether or not to convert single Variables
      with no slice info into Tensors.

  Returns:
    A dictionary of names to the operations that must be saved under
    that name.  Variables with save_slice_info are grouped together under the
    same key in no particular order.

  Raises:
    TypeError: If the type of op_list or its elements is not supported.
    ValueError: If at least two saveables share the same name.
  """
if not isinstance(op_list, (list, tuple, set)):
    raise TypeError("Variables to save should be passed in a dict or a "
                    f"list. Got {op_list}")
# List casting is necessary to support sets.
op_list = nest.flatten(list(op_list))
# When ResourceVariables are converted to Tensors, read ops are added to the
# graph. Sorting the op_list ensures that the resulting graph is always
# constructed in a deterministic way:
op_list = sorted(op_list, key=lambda x: x.name)
names_to_saveables = {}
# pylint: disable=protected-access
for var in op_list:
    resource_or_ref_variable = (
        isinstance(var, resource_variable_ops.BaseResourceVariable) or
        isinstance(var, variables.RefVariable))

    if isinstance(var, saveable_object.SaveableObject):
        names_to_saveables[var.name] = var
    elif isinstance(var, variables.PartitionedVariable):
        if var.name in names_to_saveables:
            raise ValueError(
                f"At least two variables have the same name: {var.name}")
        names_to_saveables[var.name] = var
    elif isinstance(var, variables.Variable) and var._save_slice_info:
        name = var._save_slice_info.full_name
        if name in names_to_saveables:
            if not isinstance(names_to_saveables[name], list):
                raise ValueError("Mixing slices and non-slices with the same name: "
                                 f"{name}")
            names_to_saveables[name].append(var)
        else:
            names_to_saveables[name] = [var]
    elif isinstance(var, trackable.Trackable) and not resource_or_ref_variable:
        trackable_saveables = [
            (factory() if callable(factory) else factory)
            for factory in (
                saveable_objects_from_trackable(var, tf1_saver=True).values())]
        names_to_saveables.update(
            op_list_to_dict(trackable_saveables))
    else:
        # Variables (reference and resource) have an _in_graph_mode property
        # indicating whether they were created in a graph building context. We
        # also get Tensors when graph building, which do not have this property.
        if not getattr(var, "_in_graph_mode", True):
            if not isinstance(var, resource_variable_ops.BaseResourceVariable):
                raise ValueError(
                    "Can only save/restore ResourceVariables when eager execution "
                    f"is enabled. Got type: {type(var)}.")
            set_var = names_to_saveables.setdefault(var._shared_name, var)
            if set_var is not var:
                raise ValueError(
                    "Two different ResourceVariable objects with the same "
                    f"shared_name '{var._shared_name}' were passed to the Saver. This"
                    " likely means that they were created in different Graphs or "
                    "isolated contexts, and may not be checkpointed together.")
        else:
            if convert_variable_to_tensor:
                if isinstance(var, resource_variable_ops.BaseResourceVariable):
                    var = var._graph_element  # pylint: disable=protected-access
                else:
                    var = ops.convert_to_tensor(var, as_ref=True)
                if not _tensor_comes_from_variable(var):
                    raise TypeError(f"Variable to save is not a Variable: {var}")
            if var.op.type == "ReadVariableOp":
                name = var.op.inputs[0].op.name
            else:
                name = var.op.name
            if name in names_to_saveables:
                raise ValueError(f"At least two variables have the same name: {name}")
            names_to_saveables[name] = var

    # pylint: enable=protected-access
exit(names_to_saveables)
