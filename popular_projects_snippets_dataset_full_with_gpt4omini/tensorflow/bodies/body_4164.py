# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_backend_util.py
# Only need to explicitly shuts down TPU system in TFRT since in current
# runtime, the shutdown is done in initialization process.
if accelerator_util.is_initialized():
    accelerator_util.shutdown_accelerator_system()
