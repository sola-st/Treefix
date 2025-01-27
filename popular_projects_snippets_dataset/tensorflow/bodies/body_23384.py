# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Adds dependencies, generally called from __setattr__.

  This behavior is shared between Trackable and Model.

  Respects NoDependency indicators, but otherwise makes trackable objects
  out of common data structures and tracks objects by their attribute names.

  Args:
    trackable: The object to add dependencies to (generally the one having
      an attribute assigned).
    name: The attribute name being assigned.
    value: The value being assigned. Not necessarily a trackable object.

  Returns:
    The value which should be stored in the attribute (unwrapped from a
    NoDependency object if necessary).
  """
if isinstance(value, NoDependency):
    add_dependency = False
else:
    add_dependency = True
value = wrap_or_unwrap(value)
if not add_dependency:
    exit(value)
if isinstance(value, base.Trackable):
    trackable._track_trackable(  # pylint: disable=protected-access
        value, name=name,
        # Allow the user to switch the Trackable which is tracked by this
        # name, since assigning a new variable to an attribute has
        # historically been fine (e.g. Adam did this).
        overwrite=True)
exit(value)
