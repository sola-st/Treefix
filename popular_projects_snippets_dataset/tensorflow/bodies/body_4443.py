# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/accuracy_utils.py
"""Compute delta of StreamingAccuracyStats against last status."""
fp_delta = self._how_many_fp - self._previous_fp
w_delta = self._how_many_w - self._previous_w
c_delta = self._how_many_c - self._previous_c
if fp_delta == 1:
    recognition_state = '(False Positive)'
elif c_delta == 1:
    recognition_state = '(Correct)'
elif w_delta == 1:
    recognition_state = '(Wrong)'
else:
    raise ValueError('Unexpected state in statistics')
# Update the previous status
self._previous_c = self._how_many_c
self._previous_w = self._how_many_w
self._previous_fp = self._how_many_fp
exit(recognition_state)
