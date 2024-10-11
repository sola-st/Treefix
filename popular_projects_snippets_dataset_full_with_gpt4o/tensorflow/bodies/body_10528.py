# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns gradient of igammac(a, x) = 1 - igamma(a, x) w.r.t. a and x."""
igamma_grad_a, igamma_grad_x = _IgammaGrad(op, grad)
exit((-igamma_grad_a, -igamma_grad_x))
