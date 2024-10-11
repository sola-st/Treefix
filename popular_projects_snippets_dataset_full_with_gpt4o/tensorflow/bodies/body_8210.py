# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Create CheckpointManager(s) if a checkpoint is passed else take it."""
if isinstance(self._checkpoint_or_checkpoint_manager,
              checkpoint_management.CheckpointManager):
    self._read_checkpoint_manager = self._checkpoint_or_checkpoint_manager
    self._write_checkpoint_manager = self._checkpoint_or_checkpoint_manager
    self._api_made_checkpoint_manager = False
else:
    self._api_made_checkpoint_manager = True
    # Make CheckpointManagers. MultiWorkerMirroredStrategy requires different
    # setup on chief and on other workers.
    self._read_checkpoint_manager = checkpoint_management.CheckpointManager(
        self._checkpoint_or_checkpoint_manager,
        directory=self._checkpoint_dir,
        max_to_keep=1)

    if self._is_chief:
        self._write_checkpoint_manager = self._read_checkpoint_manager
    else:
        self._write_checkpoint_manager = (
            checkpoint_management.CheckpointManager(
                self._checkpoint_or_checkpoint_manager,
                _non_chief_checkpoint_dir(self._checkpoint_dir,
                                          self._cluster_resolver.task_id),
                max_to_keep=1))
