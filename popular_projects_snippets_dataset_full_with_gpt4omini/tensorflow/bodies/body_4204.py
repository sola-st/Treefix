# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Deprecated way to shutodwn the TPU system."""
from . import accelerator_util  # pylint: disable=g-import-not-at-top
accelerator_util.shutdown_accelerator_system()
