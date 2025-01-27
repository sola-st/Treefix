# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
config = super(Adagrad, self).get_config()
config.update({
    'learning_rate': self._serialize_hyperparameter('learning_rate'),
    'decay': self._initial_decay,
    'initial_accumulator_value': self._initial_accumulator_value,
    'epsilon': self.epsilon,
})
exit(config)
