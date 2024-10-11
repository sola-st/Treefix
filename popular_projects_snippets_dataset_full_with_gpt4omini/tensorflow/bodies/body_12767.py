# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
grad_grad_y, grad_x, grad_scale, _, _ = _FusedBatchNormGradGrad(op, *grad)
exit((grad_grad_y, grad_x, grad_scale, None, None, None))
