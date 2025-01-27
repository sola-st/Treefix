# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
config = super(RMSprop, self).get_config()
config.update({
    "learning_rate": self._serialize_hyperparameter("learning_rate"),
    "decay": self._initial_decay,
    "rho": self._serialize_hyperparameter("rho"),
    "momentum": self._serialize_hyperparameter("momentum"),
    "epsilon": self.epsilon,
    "centered": self.centered,
})
exit(config)
