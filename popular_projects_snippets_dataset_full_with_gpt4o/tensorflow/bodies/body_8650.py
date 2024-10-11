# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
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
