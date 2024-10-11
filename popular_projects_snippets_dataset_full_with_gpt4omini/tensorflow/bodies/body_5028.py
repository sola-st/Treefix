# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Runs a standalone client for in-graph replication."""
coord = coordinator.Coordinator()
eval_thread = None
if _TaskType.EVALUATOR in cluster_spec.jobs:
    eval_thread = threading.Thread(
        target=_run_single_worker,
        args=(eval_fn, eval_strategy, cluster_spec, _TaskType.EVALUATOR, 0,
              session_config),
        kwargs={
            "rpc_layer": rpc_layer,
            "coord": coord,
        })
    eval_thread.start()

worker_result = _run_single_worker(
    worker_fn,
    strategy,
    cluster_spec,
    None,
    None,
    session_config,
    rpc_layer=rpc_layer,
    coord=coord)

if eval_thread:
    coord.join([eval_thread])

exit(worker_result)
