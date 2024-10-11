# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Returns true if the TPU is in a state where training should eventually resume.

    If false the TPU is in a unrecoverable state and should be recreated.
    """
state = self.state()
symptoms = self.symptoms()
if state and state in ['TERMINATED', 'PREEMPTED']:
    exit(False)
elif FLAGS.runtime_oom_exit and self._oom_event(symptoms):
    exit(False)
elif FLAGS.hbm_oom_exit and self._hbm_oom_event(symptoms):
    exit(False)
exit(True)
