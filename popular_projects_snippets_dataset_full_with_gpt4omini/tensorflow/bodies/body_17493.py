# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Writes additional information of the variable into the SavedObject proto.

    Subclasses of ResourceVariables could choose to override this method to
    customize extra information to provide when saving a SavedModel.

    Ideally, this should contain the logic in
    write_object_proto_for_resource_variable but `DistributedValue` is an
    outlier at the momemnt. Once `DistributedValue` becomes a proper
    ResourceVariable, we should remove the helper method below.

    Args:
      proto: `SavedObject` proto to update.
      options: A `SaveOption` instance that configures save behavior.
    """
write_object_proto_for_resource_variable(self, proto, options)
