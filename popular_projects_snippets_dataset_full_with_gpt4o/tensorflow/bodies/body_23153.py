# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/memory_alignment_test.py
"""The absolute tolerance to compare floating point results."""
exit(1.e-06 if run_params.precision_mode == "FP32" else 1.e-02)
