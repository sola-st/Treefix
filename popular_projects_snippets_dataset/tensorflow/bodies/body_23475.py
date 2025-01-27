# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Check that the object is saveable before listing its dependencies."""
self._check_self_external_modification()
if self._self_non_string_key:
    raise ValueError(
        f"Unable to save the object {self} (a dictionary wrapper constructed "
        "automatically on attribute assignment). The wrapped dictionary "
        "contains a non-string key which maps to a trackable object or "
        "mutable data structure.\n\nIf you don't need this dictionary "
        "checkpointed, wrap it in a non-trackable "
        "object; it will be subsequently ignored.")
if self._self_external_modification:
    raise ValueError(
        f"Unable to save the object {self} (a dictionary wrapper constructed "
        "automatically on attribute assignment). The wrapped dictionary was "
        f"modified outside the wrapper (its final value was {self}, its value"
        " when a checkpoint dependency was added was "
        f"{self._self_last_wrapped_dict_snapshot}), which breaks "
        "restoration on object creation.\n\nIf you don't need this "
        "dictionary checkpointed, wrap it in a "
        "non-trackable object; it will be subsequently ignored.")
assert not self._dirty  # Any reason for dirtiness should have an exception.
children = super()._trackable_children(save_type, **kwargs)

if save_type == base.SaveType.SAVEDMODEL:
    # Add functions to be serialized.
    children.update(
        {key: value for key, value in self.items() if _is_function(value)})

exit(children)
