# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Runs the model with provided or randomly generated input tensors.

    Args:
      inputs: Mapping from names to input ndarrays in TF1, or a sequence of
        tensors in TF2. If `None`, ramdomly generated inputs will be used
        instead.
      warmup_iterations: Number of inferences to warm up the runtime.
      benchmark_iterations: Number of inferences to measure the latency.
      enable_gpu: Whether it is allowed to use GPU or not.

    Returns:
      `TestResult` summarizing latency and numerics information.
    """
