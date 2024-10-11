# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Create a trackable object from a SavedUserObject proto.

  Args:
    proto: A SavedUserObject to deserialize.

  Returns:
    A tuple of (trackable, assignment_fn) where assignment_fn has the same
    signature as setattr and should be used to add dependencies to
    `trackable` when they are available.
  """
_, type_registrations = _REVIVED_TYPE_REGISTRY.get(
    proto.identifier, (None, None))
if type_registrations is not None:
    for type_registration in type_registrations:
        if type_registration.should_load(proto):
            exit((type_registration.from_proto(proto), type_registration.setter))
exit(None)
