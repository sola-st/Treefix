# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Set up at the beginning of a countdown period for long grace period."""
if self._grace_period > 0 and not self._final_checkpoint_countdown:
    # A factor to provide more buffer / inaccuracy.
    # TODO(wxinyi): update buffer_factor as needed. Maybe deduct a constant.
    buffer_factor = 3
    # Timing by 2 since while the preempted worker needs to do 1 extra step
    # when time_till_final_call <=0, other workers might need to do x step
    # where 0<x<2
    self._target_time_for_termination = (
        self._received_own_sigterm_time + self._grace_period -
        buffer_factor * self._estimated_run_time * 2)
