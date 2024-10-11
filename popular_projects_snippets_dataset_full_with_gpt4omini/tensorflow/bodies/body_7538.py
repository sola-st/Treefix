# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
with self.assertRaises(ValueError):
    multi_process_runner.get_barrier()
