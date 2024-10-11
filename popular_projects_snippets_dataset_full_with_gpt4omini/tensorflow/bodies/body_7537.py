# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
multi_process_runner.run(
    fn_with_barrier,
    cluster_spec=multi_worker_test_base.create_cluster_spec(
        has_chief=True, num_workers=1),
)
