# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Gathers tensors to save to the checkpoint.

    You should only override `_serialize_to_tensors` and `_restore_from_tensors`
    if you are defining a custom resource or variable with custom ops.

    Otherwise, please store the state of your trackable in `tf.Variable` objects
    and add them to Trackable object hierarchy using `setattr` (for subclasses
    of `AutoTrackable`) or overriding the `_trackable_children` method.

    For an example of a valid implementation of these two methods, please see
    `DenseHashTable`.

    **Invalid implementation**

    ````
    class NamedTrackable(Trackable):
      def __init__(self, name: str):
        self.name = name
      def _serialize_to_tensors(self):
        return {"name": self.name}
      def _restore_from_tensors(self, restored_tensors):
        self.name = restored_tensors["name"]
    ```

    In this example, `NamedTrackable` can be saved and restored from
    checkpoints, but is incompatible with SavedModel, which tries to convert
    the serialize/restore functions into tf.functions. This fails because
    attribute assignment (`self.attr = new_value`) is not graph-friendly.

    **Suggested fix**

    ```
    class NamedTrackable(Trackable):
      def __init__(self, name: str):
        self.name = tf.Variable(name)

      def _trackable_children(self):
        return {"name": self.name}
    ```

    If the `name` attribute should be saved to the checkpoint, then convert it
    a `tf.Variable`.

    **TF1 Saver Compatibility**
    If your Trackable needs to be comatible with `tf.compat.v1.train.Saver`,
    implement `_gather_saveables_from_checkpoint`.

    Returns:
      A dictionary mapping names to tensors.
    """
raise NotImplementedError
