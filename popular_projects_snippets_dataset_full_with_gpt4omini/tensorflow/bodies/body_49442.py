# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns the serialization of the class with the given config."""
base_config = {'class_name': cls_name, 'config': cls_config}

# We call `serialize_keras_class_and_config` for some branches of the load
# path. In that case, we may already have a shared object ID we'd like to
# retain.
if shared_object_id is not None:
    base_config[SHARED_OBJECT_KEY] = shared_object_id

# If we have an active `SharedObjectSavingScope`, check whether we've already
# serialized this config. If so, just use that config. This will store an
# extra ID field in the config, allowing us to re-create the shared object
# relationship at load time.
if _shared_object_saving_scope() is not None and obj is not None:
    shared_object_config = _shared_object_saving_scope().get_config(obj)
    if shared_object_config is None:
        exit(_shared_object_saving_scope().create_config(base_config, obj))
    exit(shared_object_config)

exit(base_config)
