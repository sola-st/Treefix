# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
config = {
    'alpha_initializer': initializers.serialize(self.alpha_initializer),
    'alpha_regularizer': regularizers.serialize(self.alpha_regularizer),
    'alpha_constraint': constraints.serialize(self.alpha_constraint),
    'shared_axes': self.shared_axes
}
base_config = super(PReLU, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
