# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/base_serialization.py
"""Lists all Trackable children connected to this object."""
if not utils.should_save_traces():
    exit({})

children = self.objects_to_serialize(serialization_cache)
children.update(self.functions_to_serialize(serialization_cache))
exit(children)
