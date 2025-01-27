# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Run distribute coordinator for Estimator's `train_and_evaluate`.

  Args:
    estimator: An `Estimator` instance to train and evaluate.
    train_spec: A `TrainSpec` instance to specify the training specification.
    eval_spec: A `EvalSpec` instance to specify the evaluation and export
      specification.
    executor_cls: the evaluation executor class of Estimator.

  Raises:
    ValueError: if `distribute_coordinator_mode` is None in RunConfig.
  """
run_config = estimator.config
if not run_config._distribute_coordinator_mode:  # pylint: disable=protected-access
    raise ValueError(
        'Distribute coordinator mode is not specified in `RunConfig`.')

def _worker_fn(strategy):
    """Function for worker task."""
    local_estimator = copy.deepcopy(estimator)
    # pylint: disable=protected-access
    local_estimator._config._train_distribute = strategy
    context = dc_context.get_current_worker_context()
    _init_run_config_from_worker_context(local_estimator._config, context)
    logging.info('Updated config: %s', str(vars(local_estimator._config)))
    local_estimator._train_distribution = strategy
    # pylint: enable=protected-access

    # In the standalone client, we don't need to run hooks on all threads
    # because logging hooks on all threads may be too much on the screen; also
    # tensor passed to one hook can only be fetched with the graph where the
    # tensor is defined. Other hooks such as checkpointing hooks will added by
    # MonitoredTrainingSession.
    # TODO(yuefengz): Is there a hook that does need to run on all threads in
    # standalone client mode?
    if (run_config._distribute_coordinator_mode ==  # pylint: disable=protected-access
        dc.CoordinatorMode.INDEPENDENT_WORKER or context.is_chief):
        hooks = list(train_spec.hooks)
    else:
        hooks = []

    # Prevent estimator.train from calling distribute coordinator again. This
    # function calls estimator.train which will use distribute coordinator path
    # again if `_distribute_coordinator_mode` is set.
    local_estimator._config._distribute_coordinator_mode = None  # pylint: disable=protected-access
    local_estimator.train(
        input_fn=train_spec.input_fn,
        max_steps=train_spec.max_steps,
        hooks=hooks)

def _eval_fn(strategy):
    """Function for evaluator task."""
    local_estimator = copy.deepcopy(estimator)
    # pylint: disable=protected-access
    local_estimator._config._eval_distribute = strategy
    _init_run_config_from_worker_context(
        local_estimator._config, dc_context.get_current_worker_context())
    logging.info('Updated config: %s', str(vars(local_estimator._config)))
    local_estimator._eval_distribution = strategy

    # Prevent estimator.evaluate from calling distribute coordinator again. This
    # function calls estimator.evaluate which will use distribute coordinator
    # path again if `_distribute_coordinator_mode` is set.
    local_estimator._config._distribute_coordinator_mode = None  # pylint: disable=protected-access

    executor = executor_cls(local_estimator, train_spec, eval_spec)
    executor._start_continuous_evaluation()
    # pylint: enable=protected-access

# pylint: disable=protected-access
if (run_config._distribute_coordinator_mode ==
    dc.CoordinatorMode.STANDALONE_CLIENT):
    cluster_spec = run_config.cluster_spec
    assert cluster_spec
else:
    # The cluster_spec comes from TF_CONFIG environment variable if it is
    # INDEPENDENT_WORKER mode.
    cluster_spec = None

dc.run_distribute_coordinator(
    _worker_fn,
    run_config.train_distribute,
    _eval_fn,
    run_config.eval_distribute,
    mode=run_config._distribute_coordinator_mode,
    cluster_spec=cluster_spec,
    session_config=run_config.session_config)
