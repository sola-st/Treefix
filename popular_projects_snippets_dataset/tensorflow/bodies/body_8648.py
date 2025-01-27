# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
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
