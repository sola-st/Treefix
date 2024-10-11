# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
with generic_utils.skip_failed_serialization():
    # Store the config dictionary, which may be used when reviving the object.
    # When loading, the program will attempt to revive the object from config,
    # and if that fails, the object will be revived from the SavedModel.
    exit(generic_utils.serialize_keras_object(obj))
