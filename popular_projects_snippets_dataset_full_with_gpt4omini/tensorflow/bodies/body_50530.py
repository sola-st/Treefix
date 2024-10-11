# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# TrainingState is used to manage the training state needed for
# failure-recovery of a worker in training.
# pylint: disable=protected-access

if self.model._distribution_strategy and not isinstance(
    self.model.distribute_strategy, self._supported_strategies):
    raise NotImplementedError(
        '%s is not supported yet. '
        'Currently BackupAndRestore callback only supports empty strategy, '
        'MirroredStrategy, MultiWorkerMirroredStrategy and TPUStrategy.' %
        type(self.model.distribute_strategy).__name__)
self.model._training_state = (
    worker_training_state.WorkerTrainingState(self.model, self.backup_dir))
self._training_state = self.model._training_state
self._training_state.restore()
