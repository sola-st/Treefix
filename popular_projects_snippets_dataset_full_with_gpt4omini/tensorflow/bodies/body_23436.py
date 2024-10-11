# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
self._check_external_modification()
if self._non_append_mutation:
    raise ValueError(
        f"Unable to save the object {self} (a list wrapper constructed to "
        "track trackable TensorFlow objects). A list element was replaced "
        "(__setitem__, __setslice__), deleted (__delitem__, __delslice__), "
        "or moved (sort). In order to support restoration on object "
        "creation, tracking is exclusively for append-only data structures."
        "\n\nIf you don't need this list checkpointed, wrap it in a "
        "non-trackable object; it will be subsequently ignored.")
if self._external_modification:
    raise ValueError(
        f"Unable to save the object {self} (a list wrapper constructed to "
        "track trackable TensorFlow objects). The wrapped list was modified "
        f"outside the wrapper (its final value was {self._storage}, its value"
        " when a checkpoint dependency was added was "
        f"{self._last_wrapped_list_snapshot}), which breaks "
        "restoration on object creation.\n\nIf you don't need this list "
        "checkpointed, wrap it in a NoDependency object; it will be "
        "subsequently ignored.")
children = super()._trackable_children(save_type, **kwargs)

if save_type == base.SaveType.SAVEDMODEL:
    # Add functions to be serialized.
    children.update({
        str(key): value
        for key, value in enumerate(self)
        if _is_function(value)
    })

exit(children)
