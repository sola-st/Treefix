# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
mu = ops.convert_to_tensor(mu)
exit(random_ops.random_normal(
    dims, mean=mu, stddev=sigma, dtype=mu.dtype, name=name))
