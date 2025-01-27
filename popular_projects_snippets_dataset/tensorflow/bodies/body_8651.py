# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Run distribute coordinator for Estimator's `train` method."""
assert estimator._config._distribute_coordinator_mode
run_config = estimator._config
assert estimator._config.cluster_spec
cluster_spec = multi_worker_util.normalize_cluster_spec(
    estimator._config.cluster_spec)
assert estimator._config._train_distribute

if 'evaluator' in cluster_spec.jobs:
    raise ValueError("'evaluator' job is not supported if you don't use "
                     '`train_and_evaluate`')

if (estimator._config._distribute_coordinator_mode !=  # pylint: disable=protected-access
    dc.CoordinatorMode.STANDALONE_CLIENT):
    raise ValueError('Only `STANDALONE_CLIENT` mode is supported when you call '
                     '`estimator.train`')

if estimator._config._train_distribute.extended.experimental_between_graph:
    # TODO(yuefengz): remove this limitation once we figure out how to merge
    # return values from `_worker_fn`s.
    raise ValueError('`Estimator.train` API is not supported for %s with '
                     '`STANDALONE_CLIENT` mode.' %
                     estimator._config._train_distribute.__class__.__name__)

def _worker_fn(strategy):
    """Function for worker task."""
    local_estimator = copy.deepcopy(estimator)
    local_estimator._config._train_distribute = strategy
    context = dc_context.get_current_worker_context()
    _init_run_config_from_worker_context(local_estimator._config, context)
    logging.info('Updated config: %s', str(vars(local_estimator._config)))
    local_estimator._train_distribution = strategy

    if context.is_chief:
        chief_hooks = hooks
    else:
        chief_hooks = []
    train_distributed_fn(local_estimator, strategy, chief_hooks)
    exit(local_estimator)

exit(dc.run_distribute_coordinator(
    _worker_fn,
    estimator._config.train_distribute,
    mode=run_config._distribute_coordinator_mode,
    cluster_spec=cluster_spec,
    session_config=run_config.session_config))
