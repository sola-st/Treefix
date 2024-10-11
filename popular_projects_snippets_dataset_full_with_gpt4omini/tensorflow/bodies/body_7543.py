# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
if multi_worker_test_base.get_task_type() == 'worker':
    time.sleep(10000)
ctypes.string_at(0)  # Intentionally made seg fault.
