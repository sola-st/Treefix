# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
config = super(SGD, self).get_config()
config.update({
    "learning_rate": self._serialize_hyperparameter("learning_rate"),
    "decay": self._initial_decay,
    "momentum": self._serialize_hyperparameter("momentum"),
    "nesterov": self.nesterov,
})
exit(config)
