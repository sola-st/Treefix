# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/recognize_commands.py
"""Init the RecognizeCommands with parameters used for smoothing."""
# Configuration
self._labels = labels
self._average_window_duration_ms = average_window_duration_ms
self._detection_threshold = detection_threshold
self._suppression_ms = suppression_ms
self._minimum_count = minimum_count
# Working Variable
self._previous_results = collections.deque()
self._label_count = len(labels)
self._previous_top_label = "_silence_"
self._previous_top_time = -np.inf
