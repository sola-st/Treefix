# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Makes configurations and start watchers for using with MWMS."""
if not self._cluster_resolver.cluster_spec().jobs:
    # For local-mode MultiWorkerMirroredStrategy, an empty cluster spec is
    # passed, and coordination service is not enabled nor is it needed (since
    # it's used for cross-worker communication). Thus we will directly name
    # the worker id and is_chief properties and also skip the
    # uploading/reading from coordination service logic.
    self._local_mode = True
    self._id_in_cluster = 'single_worker'
    self._is_chief = True
else:
    self._local_mode = False
    self._id_in_cluster = str(
        multi_worker_util.id_in_cluster(
            self._cluster_resolver.cluster_spec(),
            self._cluster_resolver.task_type,
            self._cluster_resolver.task_id))
    self._is_chief = multi_worker_util.is_chief(
        cluster_spec=self._cluster_resolver.cluster_spec(),
        task_type=self._cluster_resolver.task_type,
        task_id=self._cluster_resolver.task_id)
# The number of calls to `PreemptionCheckpointHandler.run` when the latest
# checkpoint was saved.
self._checkpointed_runs = variables.Variable(
    initial_value=constant_op.constant(0, dtype=dtypes.int64),
    trainable=False,
    name=_ITERATION_VARIABLE)

self._maybe_create_checkpoint_manager()

if not hasattr(self._write_checkpoint_manager._checkpoint,  # pylint: disable=protected-access
               _ITERATION_VARIABLE):
    setattr(self._write_checkpoint_manager._checkpoint, _ITERATION_VARIABLE,  # pylint: disable=protected-access
            self._checkpointed_runs)

if not hasattr(self._read_checkpoint_manager._checkpoint,  # pylint: disable=protected-access
               _ITERATION_VARIABLE):
    setattr(self._read_checkpoint_manager._checkpoint, _ITERATION_VARIABLE,  # pylint: disable=protected-access
            self._checkpointed_runs)

self._read_checkpoint_manager.restore_or_initialize()

# grace period countdown. Set to True for all workers once they finish
# timing saving a checkpoint. Once entering this phase, new
# preemption/maintenance notice will not be handled, since the whole cluster
# goes down as the worker who first initiates the grace period goes down.
self._final_checkpoint_countdown = False

self._estimated_run_time = 0

# An internal step counter that's restored to checkpointed_iterations when
# training is restored. It increments by one every time
# `PreemptionCheckpointHandler.run` is called. Note that in this case, the
# user must pass a single-step training function to
# `PreemptionCheckpointHandler.run` instead of a multiple-step one.
self._run_counter = self._checkpointed_runs.numpy()

# The worker itself has received preeption signal.
self._received_own_sigterm = threading.Event()

# Some member (could be oneself) has received preemption signal, and the
# step number to save a checkpoint has been aligned.
self._received_checkpoint_step = threading.Event()

distribution_strategy_api_counter.get_cell(
    self._platform_device.name,
    'PreemptionCheckpointHandler').increase_by(1)

if not self._local_mode:
    # When training is interrupted, we explicitly call the cleanup methods for
    # the thread watching for local worker's termination signal and the thread
    # watching for clusterwise information before we save a checkpoint and
    # exit. In the final chapter of the training where no interruption is
    # encountered, we rely on __del__ to clean up. However, there is no
    # guarantee when or whether __del__ is executed, thus we make the threads
    # daemon to avoid it preventing program from exit.
    self._cluster_wise_termination_watcher_thread = threading.Thread(
        target=self._watch_step_to_save_key,
        name='PeerTerminationWatcher-%s' % self._id_in_cluster,
        daemon=True)
    logging.info('Start watcher for peer\'s signal.')
    self._cluster_wise_termination_watcher_thread.start()

else:
    self._cluster_wise_termination_watcher_thread = None

self._poll_termination_signal_thread = None

if self._termination_watcher_fn:
    self._start_polling_for_termination_signal()
else:
    self._start_watching_for_signal()
