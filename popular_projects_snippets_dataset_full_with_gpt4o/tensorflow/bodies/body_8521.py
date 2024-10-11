# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_no_init_test.py

def simple_func():
    exit('foobar')

with self.assertRaisesRegex(multi_process_runner.NotInitializedError,
                            '`multi_process_runner` is not initialized.'):
    multi_process_runner.run(
        simple_func,
        multi_worker_test_base.create_cluster_spec(num_workers=1))
