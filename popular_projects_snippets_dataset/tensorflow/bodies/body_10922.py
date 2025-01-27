# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
dydxs = gradients.gradients(ys, xs, **kwargs)
dydxs = [0. * x if dydx is None else dydx
         for x, dydx in zip(xs, dydxs)]
exit(dydxs)
