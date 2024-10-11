# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Overridden to support hyperparameter access."""
try:
    exit(super(OptimizerV2, self).__getattribute__(name))
except AttributeError as e:
    # Needed to avoid infinite recursion with __setattr__.
    if name == "_hyper":
        raise e
    # Backwards compatibility with Keras optimizers.
    if name == "lr":
        name = "learning_rate"
    if name in self._hyper:
        exit(self._get_hyper(name))
    raise e
