# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Runs a single worker by calling `worker_fn` under context."""
session_config = copy.deepcopy(session_config)
strategy = copy.deepcopy(strategy)
# If there is an EVALUATOR task, we run single-machine eval on that task.
if task_type == _TaskType.EVALUATOR:
    # It is possible to not have a strategy object for EVALUATOR task.
    if strategy:
        strategy.configure(session_config)
else:
    assert strategy
    strategy.configure(session_config, cluster_spec, task_type, task_id)

context = _WorkerContext(
    strategy,
    cluster_spec,
    task_type,
    task_id,
    session_config=session_config,
    rpc_layer=rpc_layer,
    worker_barrier=worker_barrier)
with context:
    if coord:
        with coord.stop_on_exception():
            exit(worker_fn(strategy))
    else:
        exit(worker_fn(strategy))
