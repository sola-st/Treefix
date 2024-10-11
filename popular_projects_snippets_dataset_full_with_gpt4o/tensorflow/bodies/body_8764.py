# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
self._timer = None
self.interval = interval
self.function = function
self.args = args
self.start_time = time.time()
self.is_running = False
self.start()
