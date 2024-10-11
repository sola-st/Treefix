# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
return_value = multi_process_runner.run(
    fn_that_returns_args_and_kwargs,
    multi_worker_test_base.create_cluster_spec(num_workers=1),
    args=('a', 'b'),
    kwargs={
        'c_k': 'c_v'
    }).return_value
self.assertEqual(return_value[0][0], 'a')
self.assertEqual(return_value[0][1], 'b')
self.assertEqual(return_value[0][2], ('c_k', 'c_v'))
