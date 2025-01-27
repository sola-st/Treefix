# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
runner = multi_process_runner.MultiProcessPoolRunner(
    cluster_spec, initializer=lambda: fn_that_sets_global(1))
result = runner.run(fn_that_sets_global, args=(2,))
self.assertAllEqual(result, [1, 1])
