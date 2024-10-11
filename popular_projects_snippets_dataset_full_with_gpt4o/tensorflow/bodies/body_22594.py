# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
"""Construct a sync_replicas optimizer.

    Args:
      opt: The actual optimizer that will be used to compute and apply the
        gradients. Must be one of the Optimizer classes.
      replicas_to_aggregate: number of replicas to aggregate for each variable
        update.
      total_num_replicas: Total number of tasks/workers/replicas, could be
        different from replicas_to_aggregate.
        If total_num_replicas > replicas_to_aggregate: it is backup_replicas +
        replicas_to_aggregate.
        If total_num_replicas < replicas_to_aggregate: Replicas compute
        multiple batches per update to variables.
      variable_averages: Optional `ExponentialMovingAverage` object, used to
        maintain moving averages for the variables passed in
        `variables_to_average`.
      variables_to_average: a list of variables that need to be averaged. Only
        needed if variable_averages is passed in.
      use_locking: If True use locks for update operation.
      name: string. Optional name of the returned operation.
    """
if total_num_replicas is None:
    total_num_replicas = replicas_to_aggregate

super(SyncReplicasOptimizer, self).__init__(use_locking, name)
logging.info(
    "SyncReplicasV2: replicas_to_aggregate=%s; total_num_replicas=%s",
    replicas_to_aggregate, total_num_replicas)
self._opt = opt
self._replicas_to_aggregate = replicas_to_aggregate
self._gradients_applied = False
self._variable_averages = variable_averages
self._variables_to_average = variables_to_average
self._total_num_replicas = total_num_replicas
self._tokens_per_step = max(total_num_replicas, replicas_to_aggregate)
self._global_step = None
self._sync_token_queue = None

# The synchronization op will be executed in a queue runner which should
# only be executed by one of the replicas (usually the chief).
self._chief_queue_runner = None

# Remember which accumulator is on which device to set the initial step in
# the accumulator to be global step. This list contains list of the
# following format: (accumulator, device).
self._accumulator_list = []
