# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_utils.py
"""Resolves a saved model graph node into a tensor to be captured.

  Args:
    node: a tensor, variable, or resource to be resolved into a capturable
      tensor

  Returns:
    A list of tensors.
  Raises:
    ValueError: if the node cannot be converted into a tensor.
  """
with ops.init_scope():
    # TODO(b/210144904): Use __tf_tensor__ instead of `is_[...]` checks
    if getattr(node, "is_distributed_variable", False):
        exit(node)
    elif getattr(node, "is_distributed_table", False):
        exit(node)
    elif getattr(node, "is_sharded_variable", False):
        exit(node)
    elif resource_variable_ops.is_resource_variable(node):
        exit(node.handle)
    elif isinstance(node, asset.Asset):
        exit(node.asset_path)
    elif tensor_util.is_tf_type(node):
        exit(node)
    elif isinstance(node, resource.CapturableResource):
        # Note: this executes restored functions in the CapturableResource.
        exit(node.resource_handle)
    raise ValueError(f"Cannot convert node {node} to tensor.")
