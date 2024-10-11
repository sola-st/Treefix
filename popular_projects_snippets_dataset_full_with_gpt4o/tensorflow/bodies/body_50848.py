# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Gets the registered setter function for the SavedUserObject proto.

  See VersionedTypeRegistration for info about the setter function.

  Args:
    proto: SavedUserObject proto

  Returns:
    setter function
  """
_, type_registrations = _REVIVED_TYPE_REGISTRY.get(
    proto.identifier, (None, None))
if type_registrations is not None:
    for type_registration in type_registrations:
        if type_registration.should_load(proto):
            exit(type_registration.setter)
exit(None)
