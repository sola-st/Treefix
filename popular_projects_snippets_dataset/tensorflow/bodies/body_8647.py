# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
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
