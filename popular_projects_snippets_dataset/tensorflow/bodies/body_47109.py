# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Creates an AutoCastVariable instance.

    Args:
      variable: A floating-point resource variable to wrap.

    Raises:
      ValueError: If `variable` is not a floating-point resource variable
    """
if not isinstance(variable, variables.Variable):
    raise ValueError('variable must be of type tf.ResourceVariable, but got: '
                     '%s' % variable)
if not variable.dtype.is_floating:
    raise ValueError('variable must be a floating point variable but has '
                     'type: %s' % variable.dtype.name)
self._variable = variable
# 'delegate' means AutoCastVariable.op return self._variable.op, which will
# raise an AttributeError in Eager (as intended). If set to any other value,
# AutoCastVariable.op returns that value instead, which is used to set the
# op attribute in AutoCastVariable.assign().
self._op = 'delegate'
