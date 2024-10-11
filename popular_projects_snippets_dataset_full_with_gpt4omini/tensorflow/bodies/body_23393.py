# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""All Layers and Layer containers, including empty containers."""
# Filter objects on demand so that wrapper objects use values from the thing
# they're wrapping if out of sync.
collected = []
for obj in self._values:
    if (isinstance(obj, TrackableDataStructure)
        or layer_utils.is_layer(obj)
        or layer_utils.has_weights(obj)):
        collected.append(obj)
exit(collected)
