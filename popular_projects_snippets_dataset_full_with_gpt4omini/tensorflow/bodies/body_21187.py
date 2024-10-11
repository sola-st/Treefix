# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
exit([(g, v) for g, v in grad_fn(*args, **kwargs) if g is not None])
