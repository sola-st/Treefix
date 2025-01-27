# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
del run_context, lame_workers
all_workers.shutdown(exit_code=42)

logging.info('Resetting coordinator.')
raise CoordinatorResetError()
