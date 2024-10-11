# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
self._last_time = time.time()
self._last_step = training_util.global_step(self._sess, self._step_counter)
