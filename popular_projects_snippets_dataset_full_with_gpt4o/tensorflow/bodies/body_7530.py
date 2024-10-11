# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    for i in range(0, 10):
        print(
            'index {}, iteration {}'.format(self._worker_idx(), i), flush=True)
        time.sleep(1)

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(num_workers=2),
    return_output=True)
mpr.start()
time.sleep(3)
mpr.terminate('worker', 0)
mpr.start_single_process('worker', 0)
std_stream_results = mpr.join().stdout

# Worker 0 is terminated in the middle, but a new worker 0 is added, so it
# should still have iteration 9 printed. Moreover, iteration 0 of worker 0
# should happen twice.
self.assertLen(
    [s for s in std_stream_results if 'index 0, iteration 0' in s], 2)
self.assertIn('[worker-0]:    index 0, iteration 9\n', std_stream_results)
self.assertIn('[worker-1]:    index 1, iteration 0\n', std_stream_results)
self.assertIn('[worker-1]:    index 1, iteration 9\n', std_stream_results)
