# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/ftrl.py
config = super(Ftrl, self).get_config()
config.update({
    'learning_rate':
        self._serialize_hyperparameter('learning_rate'),
    'decay':
        self._initial_decay,
    'initial_accumulator_value':
        self._initial_accumulator_value,
    'learning_rate_power':
        self._serialize_hyperparameter('learning_rate_power'),
    'l1_regularization_strength':
        self._serialize_hyperparameter('l1_regularization_strength'),
    'l2_regularization_strength':
        self._serialize_hyperparameter('l2_regularization_strength'),
    'beta':
        self._serialize_hyperparameter('beta'),
    'l2_shrinkage_regularization_strength':
        self._l2_shrinkage_regularization_strength,
})
exit(config)
