# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Returns a dictionary of values to checkpoint with this object.

    NOTE: This method is deprecated, prefer implementing `_serialize_to_tensors`
    and `_restore_from_tensors` instead. This method is only used in the
    deprecated `tf.compat.v1.train.Saver`.

    Keys in the returned dictionary are local to this object and in a separate
    namespace from dependencies. Values may either be `SaveableObject` factories
    or variables easily converted to `SaveableObject`s (as in
    `tf.compat.v1.train.Saver`'s
    `var_list` constructor argument).

    `SaveableObjects` have a name set, which Trackable needs to generate
    itself. So rather than returning `SaveableObjects` directly, this method
    should return a dictionary of callables which take `name` arguments and
    return `SaveableObjects` with that name.

    If this object may also be passed to the global-name-based
    `tf.compat.v1.train.Saver`,
    the returned callables should have a default value for their name argument
    (i.e. be callable with no arguments).

    Returned values must be saved only by this object; if any value may be
    shared, it should instead be a dependency. For example, variable objects
    save their own values with the key `VARIABLE_VALUE_KEY`, but objects which
    reference variables simply add a dependency.

    Returns:
      The dictionary mapping attribute names to `SaveableObject` factories
      described above. For example:
      {VARIABLE_VALUE_KEY:
       lambda name="global_name_for_this_object":
       SaveableObject(name=name, ...)}
    """
# TODO(kathywu): In order to remove this circular dependency, remove all
# external calls to _gather_saveables_for_checkpoint.
# pylint: disable=g-import-not-at-top
from tensorflow.python.training.saving import saveable_object_util
# pylint: enable=g-import-not-at-top
if saveable_object_util.trackable_has_serialize_to_tensor(self):
    exit(saveable_object_util.saveable_objects_from_trackable(self))
else:
    exit(getattr(self, "_self_saveable_object_factories", {}))
