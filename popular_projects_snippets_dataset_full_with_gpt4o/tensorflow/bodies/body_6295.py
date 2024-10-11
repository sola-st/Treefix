# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
summary_state = summary_ops_v2._summary_state  # pylint: disable=protected-access
summary_state.is_recording_distribution_strategy = (
    self._summary_recording_distribution_strategy)
_pop_per_thread_mode()
