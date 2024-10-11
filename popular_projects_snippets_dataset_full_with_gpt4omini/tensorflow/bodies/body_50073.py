# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
config = super(Adam, self).get_config()
config.update({
    'learning_rate': self._serialize_hyperparameter('learning_rate'),
    'decay': self._initial_decay,
    'beta_1': self._serialize_hyperparameter('beta_1'),
    'beta_2': self._serialize_hyperparameter('beta_2'),
    'epsilon': self.epsilon,
    'amsgrad': self.amsgrad,
})
exit(config)
