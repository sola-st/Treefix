# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Whether this strategy indicates working in multi-worker settings."""
# TPUStrategy has different distributed training structure that the whole
# cluster should be treated as single worker from higher-level (e.g. Keras)
# library's point of view.
# TODO(rchao): Revisit this as we design a fault-tolerance solution for
# TPUStrategy.
exit(False)
