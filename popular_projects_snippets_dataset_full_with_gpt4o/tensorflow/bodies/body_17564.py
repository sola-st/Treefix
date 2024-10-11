# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Writes additional information of the variable into the SavedObject proto.

  This allows users to define a `hook` to provide extra information of the
  variable to the SavedObject.

  For example, DistributedVariable class would fill in components in the
  distributed context.

  Args:
    resource_variable: A `ResourceVariable` or `DistributedValue` that has the
      information to be saved into the proto.
    proto: `SavedObject` proto to update.
    options: A `SaveOption` instance that configures save behavior.
    enforce_naming: A bool determining whether to check that names end in the
      expected string ':0'
  """
proto.variable.SetInParent()
if enforce_naming and not resource_variable.name.endswith(":0"):
    raise ValueError(f"Cowardly refusing to save variable "
                     f"{resource_variable.name} because of "
                     f"unexpected suffix in the name (expected ':0')"
                     f"which won't be restored.")
proto.variable.name = meta_graph._op_name(resource_variable.name)  # pylint: disable=protected-access
proto.variable.trainable = resource_variable.trainable
proto.variable.dtype = resource_variable.dtype.as_datatype_enum
proto.variable.synchronization = resource_variable.synchronization.value
proto.variable.aggregation = resource_variable.aggregation.value
proto.variable.shape.CopyFrom(resource_variable.shape.as_proto())
if options.experimental_variable_policy._save_variable_devices(  # pylint: disable=protected-access
):
    if hasattr(resource_variable, "device"):
        proto.variable.device = resource_variable.device
