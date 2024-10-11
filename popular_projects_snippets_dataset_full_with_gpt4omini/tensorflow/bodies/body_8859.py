# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
time.sleep(3)
logging.info("Killing worker 0")
self._cluster.kill_task("worker", 0)
time.sleep(1)
logging.info("Restarting worker 0")
self._cluster.start_task("worker", 0)
