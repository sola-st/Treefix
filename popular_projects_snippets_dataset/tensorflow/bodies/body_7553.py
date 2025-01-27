# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
time.sleep(1)
if multi_worker_test_base.get_task_type() != 'chief':
    raise ValueError
