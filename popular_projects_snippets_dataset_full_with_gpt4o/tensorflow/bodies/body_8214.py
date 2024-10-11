# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Claim earliest preemption if no one else has done it before."""
if self._local_mode:
    logging.info('Member %s has received termination notice.',
                 self._id_in_cluster)
    self._received_own_sigterm_time = time.time()
    self._received_own_sigterm.set()
    exit()

try:
    context.context().set_config_key_value(_PREEMPTION_WORKER_KEY,
                                           self._id_in_cluster)
    logging.info('Member %s has received termination notice.',
                 self._id_in_cluster)
    self._received_own_sigterm_time = time.time()
    self._received_own_sigterm.set()

# This is to handle the case that a worker has received termination
# notice but hasn't come to the next step to set the step key. Other
# workers might receive a termination notice too, and attempt to set the
# config key again, which causes this error. This can be safely ignored
# since checkpoint should be saved as early as the earliest call is made.
except errors.AlreadyExistsError:
    logging.info('Member %s has received termination notice. But some other '
                 'worker has received it as well! Leaving'
                 ' it to them to decide when to checkpoint. ',
                 self._id_in_cluster)
    exit()
