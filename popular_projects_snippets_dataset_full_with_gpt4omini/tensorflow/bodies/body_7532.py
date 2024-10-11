# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    for i in range(5):
        logging.info('(logging) %s-%d, i: %d',
                     multi_worker_test_base.get_task_type(), self._worker_idx(),
                     i)
        print(
            '(print) {}-{}, i: {}'.format(
                multi_worker_test_base.get_task_type(), self._worker_idx(), i),
            flush=True)
        time.sleep(1)

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(
        has_chief=True, num_workers=2, num_ps=2),
    return_output=True)
mpr._dependence_on_chief = False

mpr.start()
mpr.start_single_process('worker', 2)
mpr.start_single_process('ps', 2)
mpr_result = mpr.join()

list_to_assert = mpr_result.stdout

for job in ['chief']:
    for iteration in range(5):
        self.assertTrue(
            any('(logging) {}-0, i: {}'.format(job, iteration) in line
                for line in list_to_assert))
        self.assertTrue(
            any('(print) {}-0, i: {}'.format(job, iteration) in line
                for line in list_to_assert))

for job in ['worker', 'ps']:
    for iteration in range(5):
        for task in range(3):
            self.assertTrue(
                any('(logging) {}-{}, i: {}'.format(job, task, iteration) in line
                    for line in list_to_assert))
            self.assertTrue(
                any('(print) {}-{}, i: {}'.format(job, task, iteration) in line
                    for line in list_to_assert))
        task = 3
        self.assertFalse(
            any('(logging) {}-{}, i: {}'.format(job, task, iteration) in line
                for line in list_to_assert))
        self.assertFalse(
            any('(print) {}-{}, i: {}'.format(job, task, iteration) in line
                for line in list_to_assert))
