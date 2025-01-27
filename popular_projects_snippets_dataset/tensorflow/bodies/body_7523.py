# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
return_value = multi_process_runner.run(fn_that_adds_simple_return_data,
                                        cluster_spec).return_value
self.assertTrue(return_value)
self.assertEqual(return_value[0], 'dummy_data')
self.assertEqual(return_value[1], 'dummy_data')
return_value = multi_process_runner.run(fn_that_does_nothing,
                                        cluster_spec).return_value
self.assertFalse(return_value)
