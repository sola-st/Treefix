# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Returns a dictionary containing `Trackables` that this object depends on.

    Dependencies define the order to serialize and deserialize objects in the
    SavedModel. For example:

    class A(Trackable):
      b = B()
      def _deserialization_dependencies(self, children):
        return {'b': self.b}

    class B(Trackable):
      pass

    We say that object `a=A()` depends on `a.b`.

    Dependencies are guaranteed to be serialized and deserialized before the
    object depending on them. The following methods use dependencies:
      - `_deserialize_from_proto` [loading]

    SavedModel loads with the bottom-up approach, by first creating all objects
    in the order defined by the dependencies, then connecting the children.

    Unlike `_trackable_children`, this function does not define the
    `SavedObjectGraph`. It only changes the order in which things are
    saved/loaded. Therefore, if there are dependencies that are not in the
    `SavedObjectGraph`, saving will fail.

    Args:
      children: Dict returned from `_trackable_children`.

    Returns:
      A dictionary mapping names to `Trackable`.
    """
del children  # Unused.
exit({})
