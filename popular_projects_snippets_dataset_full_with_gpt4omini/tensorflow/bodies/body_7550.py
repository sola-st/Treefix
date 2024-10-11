# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn(counter):
    counter.value += 1
    if counter.value == 1:
        raise ValueError

manager = multi_process_runner.manager()
counter = manager.Value(int, 0)
mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(num_workers=1),
    args=(counter,),
    auto_restart=True)
mpr.start()
mpr.join()
self.assertEqual(counter.value, 2)
