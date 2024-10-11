# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
with self.thread_coord.stop_on_exception():
    with ops.device("/job:worker/replica:0/task:0"):
        for _ in range(3):
            for _ in range(3):
                worker_train_fn()
            time.sleep(5)
