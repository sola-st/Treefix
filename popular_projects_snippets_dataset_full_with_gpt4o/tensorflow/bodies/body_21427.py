# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
with self._coord.stop_on_exception():
    self.start_loop()
    if self._timer_interval_secs is None:
        # Call back-to-back.
        while not self._coord.should_stop():
            self.run_loop()
    else:
        # Next time at which to call run_loop(), starts as 'now'.
        next_timer_time = time.time()
        while not self._coord.wait_for_stop(next_timer_time - time.time()):
            next_timer_time += self._timer_interval_secs
            self.run_loop()
    self.stop_loop()
