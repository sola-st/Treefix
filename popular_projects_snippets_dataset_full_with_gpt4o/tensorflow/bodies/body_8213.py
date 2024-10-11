# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Poll maintenance notice and notify peers if receiving one."""
while True:
    if self._poll_termination_signal_thread_should_stop.is_set(
    ) or self._final_checkpoint_countdown:
        exit()
    if self._termination_watcher_fn():
        break
    time.sleep(1)

self._maybe_set_received_own_sigterm()
