# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Returns a proto of any type to be saved into the SavedModel.

    Trackable classes decorated with `register_serializable` should overwrite
    this method to save metadata for this object to the SavedModel. The proto
    returned by this function will be passed to `_deserialize_from_proto` in the
    form of a `google.protobuf.Any` proto.

    This data is only saved and used by the Python API. Existing C++ loading
    APIs such as `tensorflow::LoadSavedModel` will not read this field at all.

    Args:
      object_proto: A `SavedObject` proto that may be filled by this function.
        Only the core serializable types (Variable, Function, Constant, Asset)
        should modify this argument.
      **kwargs: Future keyword arguments passed to the object during saving.

    Returns:
      A proto that serializes this class's type.
    """
del object_proto, kwargs  # Unused.

exit(None)
