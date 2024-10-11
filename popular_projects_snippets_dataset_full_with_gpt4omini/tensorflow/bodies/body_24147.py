# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
if self._default_session_context_manager is None:
    self._default_session_context_manager = self.as_default()
exit(self._default_session_context_manager.__enter__())
