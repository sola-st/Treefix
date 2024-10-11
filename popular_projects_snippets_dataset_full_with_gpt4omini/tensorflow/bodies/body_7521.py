# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
mpr_result = multi_process_runner.run(
    fn_that_adds_task_type_in_return_data,
    multi_worker_test_base.create_cluster_spec(
        num_workers=2, num_ps=3, has_chief=True))

job_count_dict = {'worker': 2, 'ps': 3, 'chief': 1}
for data in mpr_result.return_value:
    job_count_dict[data] -= 1

self.assertEqual(job_count_dict['worker'], 0)
self.assertEqual(job_count_dict['ps'], 0)
self.assertEqual(job_count_dict['chief'], 0)
