# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
distribute_coordinator.run_distribute_coordinator(
    None,
    MockStrategy(between_graph=True),
    mode=INDEPENDENT_WORKER,
    cluster_spec=cluster_spec,
    task_type="ps",
    task_id=0)
