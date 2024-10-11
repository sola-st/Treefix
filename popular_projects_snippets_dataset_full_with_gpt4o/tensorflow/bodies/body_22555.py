# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
"""Helper method for standarizing Variable and naming.

  Args:
    var: Current graph's variable that needs to be warm-started (initialized).
      Can be either of the following: (i) `Variable` (ii) `ResourceVariable`
      (iii) list of `Variable`: The list must contain slices of the same larger
        variable. (iv) `PartitionedVariable`
    prev_tensor_name: Name of the tensor to lookup in provided `prev_ckpt`. If
      None, we lookup tensor with same name as given `var`.

  Returns:
    A tuple of the Tensor name and var.
  """
if checkpoint_utils._is_variable(var):  # pylint: disable=protected-access
    current_var_name = _infer_var_name([var])
elif (isinstance(var, list) and
      all(checkpoint_utils._is_variable(v) for v in var)):  # pylint: disable=protected-access
    current_var_name = _infer_var_name(var)
elif isinstance(var, variables_lib.PartitionedVariable):
    current_var_name = _infer_var_name([var])
    var = var._get_variable_list()  # pylint: disable=protected-access
else:
    raise TypeError(
        "var MUST be one of the following: a Variable, list of Variable or "
        "PartitionedVariable, but is {}".format(type(var)))
if not prev_tensor_name:
    # Assume tensor name remains the same.
    prev_tensor_name = current_var_name

exit((prev_tensor_name, var))
