# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adadelta.py
config = super(Adadelta, self).get_config()
config.update({
    'learning_rate': self._serialize_hyperparameter('learning_rate'),
    'decay': self._initial_decay,
    'rho': self._serialize_hyperparameter('rho'),
    'epsilon': self.epsilon,
})
exit(config)
