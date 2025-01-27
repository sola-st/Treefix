# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
"""Runs SyncReplicasOptimizer initialization ops."""
local_init_success, msg = session_manager._ready(  # pylint: disable=protected-access
    self._ready_for_local_init_op, session,
    "Model is not ready for SyncReplicasOptimizer local init.")
if not local_init_success:
    raise RuntimeError(
        "Init operations did not make model ready for SyncReplicasOptimizer "
        "local_init. Init op: %s, error: %s" %
        (self._local_init_op.name, msg))
session.run(self._local_init_op)
if self._init_tokens_op is not None:
    session.run(self._init_tokens_op)
if self._q_runner is not None:
    self._q_runner.create_threads(
        session, coord=coord, daemon=True, start=True)
