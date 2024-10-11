# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Sets up a Monitored or Hooked Session.

    Args:
      session_creator: A factory object to create session. Typically a
        `ChiefSessionCreator` or a `WorkerSessionCreator`.
      hooks: An iterable of `SessionRunHook' objects.
      should_recover: A bool. Indicates whether to recover from `AbortedError`
        and `UnavailableError` or not.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
    """
self._graph_was_finalized = ops.get_default_graph().finalized
self._hooks = hooks or []
for h in self._hooks:
    h.begin()

worker_context = distribute_coordinator_context.get_current_worker_context()
if not session_creator and worker_context:
    session_creator = worker_context.session_creator()

# Create the session.
self._coordinated_creator = self._CoordinatedSessionCreator(
    session_creator=session_creator or ChiefSessionCreator(),
    hooks=self._hooks,
    stop_grace_period_secs=stop_grace_period_secs)
if should_recover:
    self._sess = _RecoverableSession(self._coordinated_creator)
else:
    self._sess = self._coordinated_creator.create_session()
