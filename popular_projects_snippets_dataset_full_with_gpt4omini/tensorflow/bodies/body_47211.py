# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/worker_training_state.py
self._model = model

# The epoch at which the checkpoint is saved. Used for fault-tolerance.
# GPU device only has int64 dtype registered VarHandleOp.
self._ckpt_saved_epoch = variables.Variable(
    initial_value=constant_op.constant(
        CKPT_SAVED_EPOCH_UNUSED_VALUE, dtype=dtypes.int64),
    name='ckpt_saved_epoch')

# Variable initialization.
backend.set_value(self._ckpt_saved_epoch, CKPT_SAVED_EPOCH_UNUSED_VALUE)

# _ckpt_saved_epoch gets tracked and is included in the checkpoint file
# when backing up.
checkpoint = trackable_util.Checkpoint(
    model=self._model, ckpt_saved_epoch=self._ckpt_saved_epoch)

# If this is single-worker training, checkpoint_dir are the same for
# write_checkpoint_manager and read_checkpoint_manager.
#
# If this is multi-worker training, and this worker should not
# save checkpoint, we replace the write_checkpoint_manager's checkpoint_dir
# with a temp filepath, so it writes to a file that will be removed at the
# end of back_up() call. This is necessary because the SyncOnReadVariable
# needs to be synced across all the workers in order to be read, and all
# workers need to perform `save()`.
# But all workers should restore from the same checkpoint_dir as passed in
# read_checkpoint_manager.
self.read_checkpoint_manager = checkpoint_management.CheckpointManager(
    checkpoint,
    directory=os.path.join(checkpoint_dir, 'chief'),
    max_to_keep=1)
write_checkpoint_dir = distributed_file_utils.write_dirpath(
    checkpoint_dir, self._model.distribute_strategy)
if self._model.distribute_strategy.extended.should_checkpoint:
    self.write_checkpoint_manager = self.read_checkpoint_manager
else:
    self.write_checkpoint_manager = checkpoint_management.CheckpointManager(
        checkpoint, directory=write_checkpoint_dir, max_to_keep=1)
