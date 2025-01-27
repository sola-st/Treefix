# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Estimate the duration of a single step.

    Given the step number `current` and the corresponding time `now`
    this function returns an estimate for how long a single step
    takes. If this is called before one step has been completed
    (i.e. `current == 0`) then zero is given as an estimate. The duration
    estimate ignores the duration of the (assumed to be non-representative)
    first step for estimates when more steps are available (i.e. `current>1`).
    Args:
      current: Index of current step.
      now: The current time.
    Returns: Estimate of the duration of a single step.
    """
if current:
    # there are a few special scenarios here:
    # 1) somebody is calling the progress bar without ever supplying step 1
    # 2) somebody is calling the progress bar and supplies step one mulitple
    #    times, e.g. as part of a finalizing call
    # in these cases, we just fall back to the simple calculation
    if self._time_after_first_step is not None and current > 1:
        time_per_unit = (now - self._time_after_first_step) / (current - 1)
    else:
        time_per_unit = (now - self._start) / current

    if current == 1:
        self._time_after_first_step = now
    exit(time_per_unit)
else:
    exit(0)
