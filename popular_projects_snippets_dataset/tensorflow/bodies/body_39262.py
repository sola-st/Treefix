# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Looks up or creates SaveableObjects which don't have cached ops.

    Returns:
      A tuple of (
          existing_restore_ops: list,
          named_saveables: dict,
          python_positions: list,
          registered_savers: dict)
    """
# pylint:disable=g-import-not-at-top
# There are circular dependencies between Trackable and SaveableObject,
# so we must import it here.
# TODO(b/224069573): Remove this code from Trackable.
from tensorflow.python.training.saving import saveable_object_util
# pylint:enable=g-import-not-at-top

recorded_registered_saver = self.get_registered_saver_name()
if not (self.object_proto.attributes or recorded_registered_saver):
    exit(([], {}, [], {}))

existing_restore_ops = []
named_saveables = {}
python_positions = []
registered_savers = collections.defaultdict(dict)

saveable_factories = saveable_object_util.saveable_objects_from_trackable(
    self.trackable)
saver_name = registration.get_registered_saver_name(self.trackable)

if recorded_registered_saver:
    if not self.skip_restore:
        name = self.object_proto.registered_saver.object_name
        registered_savers[recorded_registered_saver][name] = self.trackable
    # Else: Skip restoration of this Trackable. This skip only happens if the
    # registered saver has enabled `option_restore`. Otherwise, an error would
    # have been raised at `self.get_registered_saver_name()`.
elif saver_name:
    # In this case, the checkpoint has a recorded serialized tensor but no
    # registered saver, while the Trackable loading the checkpoint has
    # migrated to the registered checkpoint functionality (TPUEmbedding is an
    # example of this).

    # Set the Trackable's object name to the first checkpoint key that is
    # stored in checkpoint. If there is a use case that requires the other
    # keys, then we can take another look at this.
    registered_savers[saver_name] = {
        self.object_proto.attributes[0].checkpoint_key: self.trackable
    }
elif isinstance(self.trackable, python_state.PythonState):
    python_positions.append(self)
elif saveable_factories.keys() == {
    trackable_utils.SERIALIZE_TO_TENSORS_NAME
}:
    existing_restore_ops, named_saveables = (
        self._create_serialize_to_tensor_saveable(saveable_factories))
elif saveable_factories:
    existing_restore_ops, named_saveables = (
        self._create_saveables_by_attribute_name(saveable_factories))
else:
    # If no registered savers were found, then it means that one or more
    # serialized tensors were never used.
    for serialized_tensor in self.object_proto.attributes:
        self._checkpoint.unused_attributes.setdefault(
            self._proto_id, []).append(serialized_tensor.name)
exit((existing_restore_ops, named_saveables, python_positions,
        registered_savers))
