# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Sets execution mode for current thread."""
if mode not in (None, SYNC, ASYNC):
    raise ValueError("Execution mode should be None/SYNC/ASYNC. Got %s" %
                     mode)

if mode is None:
    mode = SYNC

enable_async = (mode == ASYNC)
if self.is_async() != enable_async:
    # Only set the execution mode if the context has already been initialized
    if self._context_handle is not None:
        self.executor.wait()
        executor_new = executor.new_executor(enable_async)
        self._thread_local_data.executor = executor_new
        pywrap_tfe.TFE_ContextSetExecutorForThread(self._context_handle,
                                                   executor_new.handle())
    else:
        self._default_is_async = enable_async
