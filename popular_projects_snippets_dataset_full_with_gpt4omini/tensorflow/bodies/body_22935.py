# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Converts the model with TensorRT and calibrates if using INT8 precision mode.

    Args:
      calibration_inputs: Mapping from input names to ndarrays in TF1. Or a
        sequence of tensors in TF2. Used as calibration data.
      num_runs: Number of calibration runs.
    """
