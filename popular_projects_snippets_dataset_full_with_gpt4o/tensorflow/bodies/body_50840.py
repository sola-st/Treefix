# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Identify a revived type version.

    Args:
      object_factory: A callable which takes a SavedUserObject proto and returns
        a trackable object. Dependencies are added later via `setter`.
      version: An integer, the producer version of this wrapper type. When
        making incompatible changes to a wrapper, add a new
        `VersionedTypeRegistration` with an incremented `version`. The most
        recent version will be saved, and all registrations with a matching
        identifier will be searched for the highest compatible version to use
        when loading.
      min_producer_version: The minimum producer version number required to use
        this `VersionedTypeRegistration` when loading a proto.
      min_consumer_version: `VersionedTypeRegistration`s with a version number
        less than `min_consumer_version` will not be used to load a proto saved
        with this object. `min_consumer_version` should be set to the lowest
        version number which can successfully load protos saved by this
        object. If no matching registration is available on load, the object
        will be revived with a generic trackable type.

        `min_consumer_version` and `bad_consumers` are a blunt tool, and using
        them will generally break forward compatibility: previous versions of
        TensorFlow will revive newly saved objects as opaque trackable
        objects rather than wrapped objects. When updating wrappers, prefer
        saving new information but preserving compatibility with previous
        wrapper versions. They are, however, useful for ensuring that
        previously-released buggy wrapper versions degrade gracefully rather
        than throwing exceptions when presented with newly-saved SavedModels.
      bad_consumers: A list of consumer versions which are incompatible (in
        addition to any version less than `min_consumer_version`).
      setter: A callable with the same signature as `setattr` to use when adding
        dependencies to generated objects.
    """
self.setter = setter
self.identifier = None  # Set after registration
self._object_factory = object_factory
self.version = version
self._min_consumer_version = min_consumer_version
self._min_producer_version = min_producer_version
if bad_consumers is None:
    bad_consumers = []
self._bad_consumers = bad_consumers
