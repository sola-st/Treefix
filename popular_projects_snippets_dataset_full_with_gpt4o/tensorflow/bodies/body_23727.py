# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Returns a new object restored by the SavedModel.

    Trackable classes decorated with `register_serializable` should overwrite
    this method to change how the object is loaded from SavedModel. By default,
    the object is initialized with no arguments.

    Example:

    ```
    def _serialize_to_proto(self, **unused_kwargs):
      return Message(name="a")

    @classmethod
    def _deserialize_from_proto(cls, proto, **unused_kwargs):
      if proto.Is(Message.DESCRIPTOR):
        unpacked = Message()
        proto.Unpack(unpacked)
        return cls(unpacked.name)
      else:
        return cls()
    ```

    This function is only used by the Python API. C++ and TensorFlow Serving do
    not have access to your registered class and cannot execute any of the
    non-tf.functions attached to the Python class. However, all signatures and
    tf.functions are still accessible.

    **Avoid creating duplicate trackables**

    SavedModel is saved by recursively gathering all of the trackables and their
    children. SavedModel loading reverses those steps by creating all
    trackables, then reconnecting the children trackables to their parents using
    `Trackable._add_trackable_child`.

    That means that if `_deserialize_from_proto` calls the `__init__` function,
    which creates all of the children trackables, then those children end up
    being created *twice*.

    To avoid this, structure your code so that Trackables are not created
    when deserialized from SavedModel:

    ```
    @register_serializable()
    class Serializable(trackable):
      def __init __(self, from_proto=False):
        create_non_trackable_objects()
        if not from_proto:
          create_variables_and_other_trackables()

      def _deserialize_from_proto(cls, **kwargs):
        return cls(from_proto=True)

      def _add_trackable_child(self, name, value):
        self.__setattr__(name, value)
    ```

    Args:
      proto: A `google.protobuf.Any` proto read from the `SavedModel`.
      dependencies: A dictionary mapping names to dependencies (see
        `_deserialization_dependencies`)
      object_proto: The `SavedObject` proto for this object.
      export_dir: The `SavedModel` directory
      asset_file_def: The `MetaGraphDef`'s `asset_file_def` field.
      operation_attributes: Dictionary mapping nodes to attribute from the
        imported `GraphDef`.
      **kwargs: Future keyword arguments passed to the object when loading.

    Returns:
      A new object.
    """
del (proto, dependencies, object_proto, export_dir, asset_file_def,
     operation_attributes, kwargs)

exit(cls())
