# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""See base class."""
if self.should_stop():
    raise RuntimeError('Run called even after should_stop requested.')

actual_fetches = {'caller': fetches}

run_context = session_run_hook.SessionRunContext(
    original_args=session_run_hook.SessionRunArgs(fetches, feed_dict),
    session=self._sess)

options = options or config_pb2.RunOptions()
feed_dict = self._call_hook_before_run(run_context, actual_fetches,
                                       feed_dict, options)

# Do session run.
run_metadata = run_metadata or config_pb2.RunMetadata()
outputs = _WrappedSession.run(
    self,
    fetches=actual_fetches,
    feed_dict=feed_dict,
    options=options,
    run_metadata=run_metadata)

for hook in self._hooks:
    hook.after_run(
        run_context,
        session_run_hook.SessionRunValues(
            results=outputs[hook] if hook in outputs else None,
            options=options,
            run_metadata=run_metadata))
self._should_stop = self._should_stop or run_context.stop_requested

exit(outputs['caller'])
