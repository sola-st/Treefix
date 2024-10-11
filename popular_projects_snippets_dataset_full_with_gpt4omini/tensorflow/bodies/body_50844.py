# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Register a type for revived objects.

  Args:
    identifier: A unique string identifying this class of objects.
    predicate: A Boolean predicate for this registration. Takes a
      trackable object as an argument. If True, `type_registration` may be
      used to save and restore the object.
    versions: A list of `VersionedTypeRegistration` objects.
  """
# Keep registrations in order of version. We always use the highest matching
# version (respecting the min consumer version and bad consumers).
versions.sort(key=lambda reg: reg.version, reverse=True)
if not versions:
    raise AssertionError("Need at least one version of a registered type.")
version_numbers = set()
for registration in versions:
    # Copy over the identifier for use in generating protos
    registration.identifier = identifier
    if registration.version in version_numbers:
        raise AssertionError(
            f"Got multiple registrations with version {registration.version} for "
            f"type {identifier}.")
    version_numbers.add(registration.version)

if identifier in _REVIVED_TYPE_REGISTRY:
    raise AssertionError(f"Duplicate registrations for type '{identifier}'")

_REVIVED_TYPE_REGISTRY[identifier] = (predicate, versions)
_TYPE_IDENTIFIERS.append(identifier)
