# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# Tasks terminated by the user should also be restarted.

def fn(counter):
    counter.value += 1
    if counter.value == 1:
        time.sleep(100)

manager = multi_process_runner.manager()
counter = manager.Value(int, 0)

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(
        has_chief=False, num_workers=1),
    args=(counter,),
    auto_restart=True)
mpr.start()
time.sleep(3)
mpr.terminate('worker', 0)
mpr.join(timeout=20)
self.assertEqual(counter.value, 2)
