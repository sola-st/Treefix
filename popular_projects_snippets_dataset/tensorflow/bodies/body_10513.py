# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of fresnel_sin(x) with respect to its argument."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    exit(grad * math_ops.sin((np.pi  / 2.) * math_ops.square(x)))
