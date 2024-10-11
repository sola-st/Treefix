# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._extended = extended

# Flag that is used to indicate whether distribution strategy is used with
# Estimator. This is required for backward compatibility of loss scaling
# when using v1 optimizer with estimator.
self._scale_loss_for_estimator = False

if not hasattr(extended, "_retrace_functions_for_each_device"):
    # pylint: disable=protected-access
    # `extended._retrace_functions_for_each_device` dictates
    # whether the same function will be retraced when it is called on
    # different devices.
    try:
        extended._retrace_functions_for_each_device = (
            len(extended.worker_devices) > 1)
        distribution_strategy_replica_gauge.get_cell("num_replicas").set(
            self.num_replicas_in_sync)
    except:  # pylint: disable=bare-except
        # Default for the case where extended.worker_devices can't return
        # a sensible value.
        extended._retrace_functions_for_each_device = True

    # Below are the dicts of axis(int) -> `tf.function`.
self._mean_reduce_helper_fns = {}
self._reduce_sum_fns = {}

# Whether this strategy is designed to work with `ClusterCoordinator`.
self._should_use_with_coordinator = False
