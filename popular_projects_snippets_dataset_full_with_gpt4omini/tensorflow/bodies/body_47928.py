# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {
    'attr_name': self.attr_name
}
base_config = super(InstanceProperty, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
