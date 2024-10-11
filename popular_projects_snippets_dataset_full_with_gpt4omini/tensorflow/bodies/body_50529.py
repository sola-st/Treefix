# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(BackupAndRestore, self).__init__()
self.backup_dir = backup_dir
self._supports_tf_logs = True
self._supported_strategies = (
    mirrored_strategy.MirroredStrategy,
    collective_all_reduce_strategy.CollectiveAllReduceStrategy,
    tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV2,
    parameter_server_strategy_v2.ParameterServerStrategyV2)

if not context.executing_eagerly():
    if ops.inside_function():
        raise ValueError('This Callback\'s method contains Python state and '
                         'should be called outside of `tf.function`s.')
    else:  # Legacy graph mode:
        raise ValueError(
            'BackupAndRestore only supports eager mode. In graph '
            'mode, consider using ModelCheckpoint to manually save '
            'and restore weights with `model.load_weights()` and by '
            'providing `initial_epoch` in `model.fit()` for fault tolerance.')

    # Only the chief worker writes model checkpoints, but all workers
    # restore checkpoint at on_train_begin().
self._chief_worker_only = False
