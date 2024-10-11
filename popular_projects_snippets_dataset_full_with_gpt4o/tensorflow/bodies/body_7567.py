# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=True, num_workers=2)
runner = multi_process_runner.MultiProcessPoolRunner(cluster_spec)
result = runner.run(fn_that_adds_task_type_in_return_data)

job_count_dict = {'worker': 2, 'chief': 1}
for data in result:
    job_count_dict[data] -= 1

self.assertEqual(job_count_dict['worker'], 0)
self.assertEqual(job_count_dict['chief'], 0)
