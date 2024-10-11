# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Tracks the given TF optimizer for initialization of its variables."""
if context.executing_eagerly():
    exit()
optimizers = _GRAPH_TF_OPTIMIZERS[None]
optimizers.add(tf_optimizer)
