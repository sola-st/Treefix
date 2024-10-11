# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
for i in range(5):
    logging.info('%s-%d, i: %d', multi_worker_test_base.get_task_type(),
                 self._worker_idx(), i)
    time.sleep(1)
