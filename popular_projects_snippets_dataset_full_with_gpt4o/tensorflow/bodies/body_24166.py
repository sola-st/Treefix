# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
# Adapt run_context and run_values to OnRunEndRequest and invoke superclass
# on_run_end()
on_run_end_request = framework.OnRunEndRequest(self._performed_action,
                                               run_values.run_metadata)
self._session_wrapper.on_run_end(on_run_end_request)
