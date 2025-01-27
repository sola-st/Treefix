# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Override setattr to support dynamic hyperparameter setting."""
# Backwards compatibility with Keras optimizers.
if name == "lr":
    name = "learning_rate"
if hasattr(self, "_hyper") and name in self._hyper:
    self._set_hyper(name, value)
else:
    super(OptimizerV2, self).__setattr__(name, value)
