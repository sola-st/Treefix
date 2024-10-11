# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context manager for setting execution mode for current thread."""
if mode is None:
    exit()
else:
    ctx = context()
    executor_new = executor.new_executor(mode == ASYNC)
    executor_old = ctx.executor
    try:
        executor_old.wait()
        ctx.executor = executor_new
        exit()
    finally:
        ctx.executor = executor_old
        executor_new.wait()
