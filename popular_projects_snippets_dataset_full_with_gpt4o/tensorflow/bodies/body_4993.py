# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
"""Restore thread local summary state from self."""
# TODO(slebedev): is this still relevant? the referenced bug is closed.
summary_state = summary_ops_v2._summary_state  # pylint: disable=protected-access
summary_state.step = self._summary_step
summary_state.writer = self._summary_writer
summary_state.is_recording = self._summary_recording
summary_state.is_recording_distribution_strategy = (
    self._summary_recording_distribution_strategy)
