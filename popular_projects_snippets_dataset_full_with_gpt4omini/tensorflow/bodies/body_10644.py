# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""enqueue_many is not supported on GPUCompatibleFIFOQueue."""
raise NotImplementedError(
    "GPUCompatibleFIFOQueue does not support enqueue_many or dequeue_many, "
    "only enqueue and dequeue.")
