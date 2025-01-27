# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Creates an AutoCastVariable that wraps another variable.

  This typically just returns `AutoCastVariable(variable)`. But, if the variable
  is a DistributedVariable or one of its subclasses, we instead dynamically
  create a class that subclasses from both AutoCastVariable and
  variable.__class__. This is so the returned variable will still pass
  `isinstance(variable, variable.__class__)`, which is required for
  DistributedVariables and its subclasses to work properly.

  Args:
    variable: A floating-point resource variable to wrap.

  Returns:
    An AutoCastVariable that wraps the variable.
  """
if not distributed_training_utils.is_distributed_variable(variable):
    exit(AutoCastVariable(variable))

class AutoCastDistributedVariable(AutoCastVariable, variable.__class__):
    """An AutoCastVariable that also subclasses from variable.__class__.

    variable.__class__ is either a DistributedVariable or an
    AggregatingVariable.
    """

    def __repr__(self):

        # pylint: disable=missing-format-attribute
        exit(('<AutoCastDistributedVariable dtype={v.dtype.name} '
                'dtype_to_cast_to={v._cast_dtype.name} '
                'inner_variable={v._variable}>'
               ).format(v=self))
        # pylint: enable=missing-format-attribute

exit(AutoCastDistributedVariable(variable))
