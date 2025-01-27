# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/watchdog_test.py
tmp_file = self.create_tempfile()
f = open(tmp_file, "w+")

triggerred_count = [0]

def on_triggered_fn():
    triggerred_count[0] += 1

timeout = 3
if use_env_var:
    os.environ["TF_CLUSTER_COORDINATOR_WATCH_DOG_TIMEOUT"] = str(timeout)
    wd = watchdog.WatchDog(traceback_file=f, on_triggered=on_triggered_fn)
else:
    wd = watchdog.WatchDog(
        timeout=timeout, traceback_file=f, on_triggered=on_triggered_fn)
time.sleep(6)

self.assertGreaterEqual(triggerred_count[0], 1)
wd.report_closure_done()
time.sleep(1)
self.assertGreaterEqual(triggerred_count[0], 1)
time.sleep(5)
self.assertGreaterEqual(triggerred_count[0], 2)

wd.stop()
time.sleep(5)
last_triggered_count = triggerred_count[0]
time.sleep(10)
self.assertEqual(last_triggered_count, triggerred_count[0])

f.close()
with open(tmp_file) as f:
    self.assertIn("Current thread", f.read())
