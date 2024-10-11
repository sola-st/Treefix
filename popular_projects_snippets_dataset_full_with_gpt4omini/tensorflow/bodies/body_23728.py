# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Restores a connection between trackables when loading from SavedModel.

    SavedModel stores both the object metadata and its list of children. When
    loading, this function is used along with `_deserialize_from_proto` to load
    objects from the SavedModel: First, all saved objects are created with
    `_deserialize_from_proto`. After that is complete, the children are
    connected using `_add_trackable_child`.

    **Example**

    `tf.Module`, `tf.keras.Model` and Keras layers use `__setattr__` to track
    children. This is why users can call `model.v = tf.Variable(...)`, and the
    variable will be automatically saved to the checkpoint. The implementation
    of this method for the listed objects is:

    ```
    def _add_trackable_child(self, name, value):
      self.__setattr__(name, value)
    ```

    Args:
      name: The name of the connection between the parent and child `Trackable`.
      value: The child `Trackable` object.
    """
self._track_trackable(value, name, overwrite=True)
