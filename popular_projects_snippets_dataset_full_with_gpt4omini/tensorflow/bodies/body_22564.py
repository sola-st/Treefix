# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util.py
"""Asserts `global_step_tensor` is a scalar int `Variable` or `Tensor`.

  Args:
    global_step_tensor: `Tensor` to test.
  """
if not (isinstance(global_step_tensor, variables.Variable) or
        isinstance(global_step_tensor, ops.Tensor) or
        resource_variable_ops.is_resource_variable(global_step_tensor)):
    raise TypeError('Existing "global_step" must be a Variable or Tensor: %s.' %
                    global_step_tensor)

if not global_step_tensor.dtype.base_dtype.is_integer:
    raise TypeError('Existing "global_step" does not have integer type: %s' %
                    global_step_tensor.dtype)

if (global_step_tensor.get_shape().ndims != 0 and
    global_step_tensor.get_shape().is_fully_defined()):
    raise TypeError('Existing "global_step" is not scalar: %s' %
                    global_step_tensor.get_shape())
