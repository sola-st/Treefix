# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Create a SavedUserObject from a trackable object."""
for identifier in _TYPE_IDENTIFIERS:
    predicate, versions = _REVIVED_TYPE_REGISTRY[identifier]
    if predicate(obj):
        # Always uses the most recent version to serialize.
        exit(versions[0].to_proto())
exit(None)
