# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
# Ideally this should be run in after_create_session but is not for the
# following reason:
# Currently there is no way of enforcing an order of running the
# `SessionRunHooks`. Hence it is possible that the `_DatasetInitializerHook`
# is run *after* this hook. That is troublesome because
# 1. If a checkpoint exists and this hook restores it, the initializer hook
#    will override it.
# 2. If no checkpoint exists, this hook will try to save an uninitialized
#    iterator which will result in an exception.
#
# As a temporary fix we enter the following implicit contract between this
# hook and the _DatasetInitializerHook.
# 1. The _DatasetInitializerHook initializes the iterator in the call to
#    after_create_session.
# 2. This hook saves the iterator on the first call to `before_run()`, which
#    is guaranteed to happen after `after_create_session()` of all hooks
#    have been run.

# Check if there is an existing checkpoint. If so, restore from it.
# pylint: disable=protected-access
latest_checkpoint_path = checkpoint_management.latest_checkpoint(
    self._checkpoint_saver_hook._checkpoint_dir,
    latest_filename=self._latest_filename)
if latest_checkpoint_path:
    self._checkpoint_saver_hook._get_saver().restore(session,
                                                     latest_checkpoint_path)
else:
    # The checkpoint saved here is the state at step "global_step".
    # Note: We do not save the GraphDef or MetaGraphDef here.
    global_step = session.run(self._checkpoint_saver_hook._global_step_tensor)
    self._checkpoint_saver_hook._save(session, global_step)
    self._checkpoint_saver_hook._timer.update_last_triggered_step(global_step)
