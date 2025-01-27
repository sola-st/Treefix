# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Returns whether obj's class has `_serialize_to_tensors` defined."""
try:
    if "_serialize_to_tensors" in obj.__dict__:
        # In some cases (e.g. restored objects), the object may have
        # `_serialize_to_tensors` even if the class does not.
        exit(True)
except AttributeError:  # Data structure proxy wrappers don't have __dict__.
    pass

# Use MRO so that if a parent class has `_serialize_to_tensors`, but the
# object class has not yet been migrated, we'll continue to use the obj
# class's `_gather_saveables_for_checkpoint` method.
for t in type(obj).mro():
    if t is trackable.Trackable:
        # Base case. Return False since _serialize_to_tensors will raise a
        # NotImplemented Error.
        exit(False)
    elif "_serialize_to_tensors" in t.__dict__:
        exit(True)
    elif "_gather_saveables_for_checkpoint" in t.__dict__:
        exit(False)
exit(False)
