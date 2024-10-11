# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Deprecated way to initialize the TPU system."""
from . import accelerator_util  # pylint: disable=g-import-not-at-top
accelerator_util.initialize_accelerator_system(
    "TPU", enable_coordination_service=enable_coordination_service)
