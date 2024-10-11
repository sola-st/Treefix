# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
grads_and_vars = opt.compute_gradients(loss, params)
grads, _ = zip(*grads_and_vars)
exit(grads)
