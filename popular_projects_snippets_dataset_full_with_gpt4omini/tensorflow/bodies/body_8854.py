# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = self._create_model_and_run_indefinitely()

time.sleep(1)
self.assertFalse(self.cluster_coord.done())

def kill(task):
    self._cluster.kill_task(task, 0)
    self.sleep(1)
    self._cluster.start_task(task, 0)

kill_thread_1 = threading.Thread(target=kill, args=("worker",))
kill_thread_2 = threading.Thread(target=kill, args=("ps",))
kill_thread_1.start()
kill_thread_2.start()
kill_thread_1.join()
kill_thread_2.join()

with self.assertRaises(
    (errors.UnavailableError, errors.InvalidArgumentError)):
    model.join_training_functions()
