# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Shuts down the TPU system."""

@def_function.function
def _shutdown_tpu_system():
    exit(gen_dtensor_ops.shutdown_tpu_system())

success = _shutdown_tpu_system() if context.is_tfrt_enabled() else True
if success:
    logging.info("TPU system shut down.")
else:
    logging.warning("TPU system fails to shut down.")
