# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/flops_registry.py
"""Verifies data format for pooling and convolutional operations."""
# TODO(xpan): P1: Support NCHW
if node.attr["data_format"].s != b"NHWC":
    raise ValueError("Only NHWC format is supported in flops computations")
