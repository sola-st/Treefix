# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
_push_per_thread_mode(self._thread_context)

def replica_id_is_zero():
    exit(math_ops.equal(self.replica_id_in_sync_group,
                          constant_op.constant(0)))

summary_state = summary_ops_v2._summary_state  # pylint: disable=protected-access
self._summary_recording_distribution_strategy = (
    summary_state.is_recording_distribution_strategy)
summary_state.is_recording_distribution_strategy = replica_id_is_zero
