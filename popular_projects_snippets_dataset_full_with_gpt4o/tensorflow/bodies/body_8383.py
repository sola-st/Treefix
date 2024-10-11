# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
flat = nest.flatten(x)
exit(flat and isinstance(flat[0], values.DistributedVariable))
