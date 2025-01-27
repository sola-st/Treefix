# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    for i in range(5):
        logging.info('%s-%d, i: %d', multi_worker_test_base.get_task_type(),
                     self._worker_idx(), i)
        time.sleep(1)

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(
        has_chief=True, num_workers=1),
    return_output=True)

def eval_func():
    time.sleep(1)
    mpr.start_single_process(task_type='evaluator', task_id=0)

eval_thread = threading.Thread(target=eval_func)
eval_thread.start()
mpr.start_in_process_as(as_task_type='chief', as_task_id=0)
eval_thread.join()
list_to_assert = mpr.join().stdout
for job in ['worker', 'evaluator']:
    for iteration in range(5):
        self.assertTrue(
            any('{}-0, i: {}'.format(job, iteration) in line
                for line in list_to_assert))
