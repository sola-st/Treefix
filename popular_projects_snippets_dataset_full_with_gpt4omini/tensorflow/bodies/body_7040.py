# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
if not container:
    cluster_spec = multi_worker_test_base.create_cluster_spec(
        has_chief=has_chief,
        num_workers=num_workers,
        num_ps=0,
        has_eval=False)
    runner = multi_process_runner.MultiProcessPoolRunner(
        cluster_spec, initializer=initializer, share_gpu=share_gpu)
    container.append(runner)
exit(container[0])
