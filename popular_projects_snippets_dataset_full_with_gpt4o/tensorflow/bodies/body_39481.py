# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Specify the checkpoint being loaded.

    Args:
      object_graph_proto: The TrackableObjectGraph protocol buffer associated
        with this checkpoint.
      save_path: A string, the path to the checkpoint, as returned by
        `tf.train.latest_checkpoint`.
      save_path_tensor: A string `Tensor` which contains or will be fed the save
        path.
      reader: A `CheckpointReader` for `save_path`. If None,
        `_CheckpointRestoreCoordinator` will initialize one itself.
      restore_op_cache: A dictionary shared between
        `_CheckpointRestoreCoordinator`s for the same Python objects, used to
        look up restore ops by name to avoid re-creating them across multiple
        `restore()` calls.
      graph_view: A graph_view_lib.ObjectGraphView object for the restored
        objects.
      options: A CheckpointOptions object.
      saveables_cache: An optional cache storing previously created
        SaveableObjects created for each Trackable. Maps Trackables to a
        dictionary of attribute names to Trackable.
    """
self.options = options
self.object_graph_proto = object_graph_proto
self.restore_uid = ops.uid()
# Maps from proto ids to lists of attributes which were in the checkpoint
# but not loaded into any object, for error checking.
self.unused_attributes = {}
# Dictionary mapping from an id in the protocol buffer flat array to
# Trackable Python objects. This mapping may be deferred if a
# checkpoint is restored before all dependencies have been tracked. Uses
# weak references so that partial restorations don't create reference cycles
# (as objects with deferred dependencies will generally have references to
# this object).
self.object_by_proto_id = weakref.WeakValueDictionary()
self.matched_proto_ids = set()
# A set of all Python objects we've seen as dependencies, even if we didn't
# use them (for example because of inconsistent references when
# loading). Used to make status assertions fail when loading checkpoints
# that don't quite match.
self.all_python_objects = object_identity.ObjectIdentityWeakSet()
self.save_path_tensor = save_path_tensor
self.save_path_string = save_path
self.dtype_map = reader.get_variable_to_dtype_map()
self.shape_map = reader.get_variable_to_shape_map()
# A NewCheckpointReader for the most recent checkpoint, for streaming Python
# state restoration.
# When graph building, contains a list of ops to run to restore objects from
# this checkpoint.
self.restore_ops = []
self.restore_ops_by_name = restore_op_cache
self.graph_view = graph_view
self.new_restore_ops_callback = None
# A mapping from optimizer proto ids to lists of slot variables to be
# restored when the optimizer is tracked. Only includes slot variables whose
# regular variables have already been created, and only for optimizer
# objects which have not yet been created/tracked.
self.deferred_slot_restorations = {}
# A mapping from variable proto ids to lists of slot variables to be
# restored when the variable is created/tracked. These get shifted over to
# deferred_slot_restorations if the optimizer hasn't been created when that
# happens.
self.slot_restorations = {}
# Controls whether errors are printed in __del__ if some objects did not
# match.
self.expect_partial_attr = False
for node_index, node in enumerate(self.object_graph_proto.nodes):
    for slot_reference in node.slot_variables:
        # `node` refers to an `Optimizer`, since only these have slot variables.
        self.slot_restorations.setdefault(
            slot_reference.original_variable_node_id, []).append(
                base._SlotVariableRestoration(  # pylint: disable=protected-access
                    optimizer_id=node_index,
                    slot_variable_id=slot_reference.slot_variable_node_id,
                    slot_name=slot_reference.slot_name))

self._deleter = _CheckpointRestoreCoordinatorDeleter(
    self.expect_partial_attr,
    self.object_graph_proto,
    self.matched_proto_ids,
    self.unused_attributes)

self.saveables_cache = saveables_cache
