# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
# Count the steps.
current_step = training_util.global_step(self._sess, self._step_counter)
added_steps = current_step - self._last_step
self._last_step = current_step
# Measure the elapsed time.
current_time = time.time()
elapsed_time = current_time - self._last_time
self._last_time = current_time
# Reports the number of steps done per second
if elapsed_time > 0.:
    steps_per_sec = added_steps / elapsed_time
else:
    steps_per_sec = float("inf")
summary = Summary(value=[
    Summary.Value(tag=self._summary_tag, simple_value=steps_per_sec)
])
if self._sv.summary_writer:
    self._sv.summary_writer.add_summary(summary, current_step)
logging.log_first_n(logging.INFO, "%s: %g", 10, self._summary_tag,
                    steps_per_sec)
