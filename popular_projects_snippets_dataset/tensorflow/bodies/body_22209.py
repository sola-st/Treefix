# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Create a `Supervisor`.

    Args:
      graph: A `Graph`.  The graph that the model will use.  Defaults to the
        default `Graph`.  The supervisor may add operations to the graph before
        creating a session, but the graph should not be modified by the caller
        after passing it to the supervisor.
      ready_op: 1-D string `Tensor`.  This tensor is evaluated by supervisors in
        `prepare_or_wait_for_session()` to check if the model is ready to use.
        The model is considered ready if it returns an empty array.  Defaults to
        the tensor returned from `tf.compat.v1.report_uninitialized_variables()`
        If `None`, the model is not checked for readiness.
      ready_for_local_init_op: 1-D string `Tensor`.  This tensor is evaluated by
        supervisors in `prepare_or_wait_for_session()` to check if the model is
        ready to run the local_init_op. The model is considered ready if it
        returns an empty array. Defaults to `None`. If `None`, the model is not
        checked for readiness before running local_init_op.
      is_chief: If True, create a chief supervisor in charge of initializing and
        restoring the model.  If False, create a supervisor that relies on a
        chief supervisor for inits and restore.
      init_op: `Operation`.  Used by chief supervisors to initialize the model
        when it can not be recovered.  Defaults to an `Operation` that
        initializes all global variables.  If `None`, no initialization is done
        automatically unless you pass a value for `init_fn`, see below.
      init_feed_dict: A dictionary that maps `Tensor` objects to feed values.
        This feed dictionary will be used when `init_op` is evaluated.
      local_init_op: `Operation`. Used by all supervisors to run initializations
        that should run for every new supervisor instance. By default these are
        table initializers and initializers for local variables. If `None`, no
        further per supervisor-instance initialization is done automatically.
      logdir: A string.  Optional path to a directory where to checkpoint the
        model and log events for the visualizer.  Used by chief supervisors. The
        directory will be created if it does not exist.
      summary_op: An `Operation` that returns a Summary for the event logs. Used
        by chief supervisors if a `logdir` was specified.  Defaults to the
        operation returned from summary.merge_all().  If `None`, summaries are
        not computed automatically.
      saver: A Saver object.  Used by chief supervisors if a `logdir` was
        specified.  Defaults to the saved returned by Saver(). If `None`, the
        model is not saved automatically.
      global_step: An integer Tensor of size 1 that counts steps.  The value
        from 'global_step' is used in summaries and checkpoint filenames.
        Default to the op named 'global_step' in the graph if it exists, is of
        rank 1, size 1, and of type tf.int32 or tf.int64.  If `None` the global
        step is not recorded in summaries and checkpoint files.  Used by chief
        supervisors if a `logdir` was specified.
      save_summaries_secs: Number of seconds between the computation of
        summaries for the event log.  Defaults to 120 seconds.  Pass 0 to
        disable summaries.
      save_model_secs: Number of seconds between the creation of model
        checkpoints.  Defaults to 600 seconds.  Pass 0 to disable checkpoints.
      recovery_wait_secs: Number of seconds between checks that the model is
        ready.  Used by supervisors when waiting for a chief supervisor to
        initialize or restore the model.  Defaults to 30 seconds.
      stop_grace_secs: Grace period, in seconds, given to running threads to
        stop when `stop()` is called.  Defaults to 120 seconds.
      checkpoint_basename: The basename for checkpoint saving.
      session_manager: `SessionManager`, which manages Session creation and
        recovery. If it is `None`, a default `SessionManager` will be created
        with the set of arguments passed in for backwards compatibility.
      summary_writer: `SummaryWriter` to use or `USE_DEFAULT`.  Can be `None` to
        indicate that no summaries should be written.
      init_fn: Optional callable used to initialize the model. Called after the
        optional `init_op` is called.  The callable must accept one argument,
        the session being initialized.
      local_init_run_options: RunOptions to be passed as the SessionManager
        local_init_run_options parameter.

    Returns:
      A `Supervisor`.

    Raises:
      RuntimeError: If called with eager execution enabled.

    @compatibility(eager)
    `Supervisor`s are not supported when eager execution is enabled.
    @end_compatibility
    """
if context.executing_eagerly():
    raise RuntimeError("Supervisors are incompatible with eager execution.")
# Set default values of arguments.
if graph is None:
    graph = ops.get_default_graph()
with graph.as_default():
    self._init_ready_op(
        ready_op=ready_op, ready_for_local_init_op=ready_for_local_init_op)
    self._init_init_op(init_op=init_op, init_feed_dict=init_feed_dict)
    self._init_local_init_op(local_init_op=local_init_op)
    self._init_saver(saver=saver)
    self._init_summary_op(summary_op=summary_op)
    self._init_global_step(global_step=global_step)
self._graph = graph
self._meta_graph_def = meta_graph.create_meta_graph_def(
    graph_def=graph.as_graph_def(add_shapes=True),
    saver_def=self._saver.saver_def if self._saver else None)
self._is_chief = is_chief
self._coord = coordinator.Coordinator()
self._recovery_wait_secs = recovery_wait_secs
self._stop_grace_secs = stop_grace_secs
self._init_fn = init_fn
self._local_init_run_options = local_init_run_options

# Set all attributes related to checkpointing and writing events to None.
# Afterwards, set them appropriately for chief supervisors, as these are
# the only supervisors that can write checkpoints and events.
self._logdir = None
self._save_summaries_secs = None
self._save_model_secs = None
self._save_path = None
self._summary_writer = None

if self._is_chief:
    self._logdir = logdir
    self._save_summaries_secs = save_summaries_secs
    self._save_model_secs = save_model_secs
    if self._logdir:
        self._save_path = os.path.join(self._logdir, checkpoint_basename)
    if summary_writer is Supervisor.USE_DEFAULT:
        if self._logdir:
            self._summary_writer = _summary.FileWriter(self._logdir)
    else:
        self._summary_writer = summary_writer
    self._graph_added_to_summary = False

self._init_session_manager(session_manager=session_manager)
self._verify_setup()
# The graph is not allowed to change anymore.
graph.finalize()
