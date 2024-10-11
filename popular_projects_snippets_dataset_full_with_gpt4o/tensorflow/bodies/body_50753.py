# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Load state from checkpoint into the deserialized objects."""
variables_path = path_helpers.get_variables_path(self._export_dir)
# TODO(b/205010730): Clean use of private methods of TrackableSaver.
# pylint: disable=protected-access
saver = checkpoint.TrackableSaver(graph_view.ObjectGraphView(self.get(0)))
with ops.device("CPU"):
    saver._file_prefix_placeholder = constant_op.constant(variables_path)
if self._save_options.allow_partial_checkpoint:
    load_status = saver.restore(variables_path,
                                self._checkpoint_options).expect_partial()
    load_status.assert_nontrivial_match()
else:
    load_status = saver.restore(variables_path, self._checkpoint_options)
    load_status.assert_existing_objects_matched()
ckpt = load_status._checkpoint

if not context.executing_eagerly():
    reader = py_checkpoint_reader.NewCheckpointReader(variables_path)

    # When running in eager mode, the `restore` call above has already run and
    # restored the state of trackables, and calling `position.restore_ops()`
    # would re-run the restore. In graph mode, that will return a cached list
    # of ops that must run to restore the object on that position. We have to
    # wire them in the initializers of the objects so that they get
    # initialized properly when using common practices (e.g. the ones used by
    # ManagedSession) without further user action.
    for object_id, obj in dict(ckpt.object_by_proto_id).items():
        position = restore.CheckpointPosition(checkpoint=ckpt,
                                              proto_id=object_id)
        registered_saver = position.get_registered_saver_name()
        if registered_saver:
            raise NotImplementedError(
                "Loading a SavedModel that uses registered checkpoint saver is "
                f"not supported in graph mode. The loaded object {obj} uses the "
                f"saver registered with the name {registered_saver}.")

        restore_ops = position.restore_ops(reader)
        if restore_ops:
            if resource_variable_ops.is_resource_variable(obj):
                if len(restore_ops) == 1:
                    obj._initializer_op = restore_ops[0]
                else:
                    obj._initializer_op = control_flow_ops.group(*restore_ops)
            elif (isinstance(obj, lookup_ops.LookupInterface) or
                  isinstance(obj, resource.CapturableResource)):
                # We don't need to check for eager execution here, since this code
                # path should only be taken if we are restoring in graph mode.
                ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, restore_ops)
            else:
                raise NotImplementedError(
                    f"Unable to restore state of object {obj} from the checkpoint.")
