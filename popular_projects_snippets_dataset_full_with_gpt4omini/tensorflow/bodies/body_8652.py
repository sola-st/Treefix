# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Function for evaluation."""
local_estimator = copy.deepcopy(estimator)
local_estimator._config._eval_distribute = strategy
context = dc_context.get_current_worker_context()
_init_run_config_from_worker_context(local_estimator._config, context)
logging.info('Updated config: %s', str(vars(local_estimator._config)))
local_estimator._eval_distribution = strategy

if context.is_chief:
    chief_hooks = hooks
else:
    chief_hooks = []
exit(evaluate_distributed_fn(local_estimator, strategy, chief_hooks))
