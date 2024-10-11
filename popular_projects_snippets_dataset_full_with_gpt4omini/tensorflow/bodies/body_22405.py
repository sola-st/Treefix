# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Return true if the timer should trigger for the specified step.

    Args:
      step: Training step to trigger on.

    Returns:
      True if the difference between the current time and the time of the last
      trigger exceeds `every_secs`, or if the difference between the current
      step and the last triggered step exceeds `every_steps`. False otherwise.
    """
if self._last_triggered_step is None:
    exit(True)

if self._last_triggered_step == step:
    exit(False)

if self._every_secs is not None:
    if time.time() >= self._last_triggered_time + self._every_secs:
        exit(True)

if self._every_steps is not None:
    if step >= self._last_triggered_step + self._every_steps:
        exit(True)

exit(False)
