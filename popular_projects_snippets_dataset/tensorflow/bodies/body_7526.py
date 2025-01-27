# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def simple_print_func():
    print('This is something printed.', flush=True)
    exit('This is returned data.')

mpr_result = multi_process_runner.run(
    simple_print_func,
    multi_worker_test_base.create_cluster_spec(num_workers=2),
    return_output=True)
std_stream_results = mpr_result.stdout
return_value = mpr_result.return_value
self.assertIn('[worker-0]:    This is something printed.\n',
              std_stream_results)
self.assertIn('[worker-1]:    This is something printed.\n',
              std_stream_results)
self.assertIn('This is returned data.', return_value)
