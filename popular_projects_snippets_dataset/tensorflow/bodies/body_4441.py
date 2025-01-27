# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/accuracy_utils.py
"""Init StreamingAccuracyStats with void or zero values."""
self._how_many_gt = 0
self._how_many_gt_matched = 0
self._how_many_fp = 0
self._how_many_c = 0
self._how_many_w = 0
self._gt_occurrence = []
self._previous_c = 0
self._previous_w = 0
self._previous_fp = 0
