# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Return whether to exit: exit if no grace period or grace period ends."""
# we should directly exit in either of the two cases:
# 1. if no grace period is provided;
# 2. if there is a grace period, and we're in countdown period. This,
# together with the fact that _received_checkpoint_step is set (again),
# means it's time to exit: when there is a grace period, a worker
# receives preemption signal and sets the step key. Then all workers
# receive the step key and set their local _received_checkpoint_step
# event, enters this branch in _check_preemption_and_maybe_checkpoint, make
# a checkpoint. Then they set _final_checkpoint_countdown to True, clear
# _received_checkpoint_step, and continue training. New preemption
# signals anywhere in the cluster will not be handled, because
# _PREEMPTION_WORKER_KEY is occupied. The only chance that
# _received_checkpoint_step gets set again is when the worker who has
# received the preemption signal earlier decide it's time to do a final
# checkpoint (by checking if it already passes
# _target_time_for_termination). It will upload a final step key. All
# workers receive this key and again set _received_checkpoint_step. So,
# if we found out that _received_checkpoint_step is set, and also
# _final_checkpoint_countdown is true, it's checkpoint and exit time.
exit((self._grace_period <= 0) or self._final_checkpoint_countdown)
