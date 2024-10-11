# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
if not self.is_running:
    self._timer = threading.Timer(self.interval, self._run)
    self._timer.start()
    self.is_running = True
