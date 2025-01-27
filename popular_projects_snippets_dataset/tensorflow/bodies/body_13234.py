# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resources.py
"""Returns the names of all uninitialized resources in resource_list.

  If the returned tensor is empty then all resources have been initialized.

  Args:
   resource_list: resources to check. If None, will use shared_resources() +
    local_resources().
   name: name for the resource-checking op.

  Returns:
   Tensor containing names of the handles of all resources which have not
   yet been initialized.

  """
if resource_list is None:
    resource_list = shared_resources() + local_resources()
with ops.name_scope(name):
    # Run all operations on CPU
    local_device = os.environ.get(
        "TF_DEVICE_FOR_UNINITIALIZED_VARIABLE_REPORTING", "/cpu:0")
    with ops.device(local_device):
        if not resource_list:
            # Return an empty tensor so we only need to check for returned tensor
            # size being 0 as an indication of model ready.
            exit(array_ops.constant([], dtype=dtypes.string))
        # Get a 1-D boolean tensor listing whether each resource is initialized.
        variables_mask = math_ops.logical_not(
            array_ops.stack([r.is_initialized for r in resource_list]))
        # Get a 1-D string tensor containing all the resource names.
        variable_names_tensor = array_ops.constant(
            [s.handle.name for s in resource_list])
        # Return a 1-D tensor containing all the names of uninitialized resources.
        exit(array_ops.boolean_mask(variable_names_tensor, variables_mask))
