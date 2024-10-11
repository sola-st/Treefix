# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
"""Pad component shapes with 1's so all components have the same rank."""
exit(tensor_shape.TensorShape(
    [1] * (self.shape.ndims - s.ndims)).concatenate(s))
