# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
config = super(AddLoss, self).get_config()
config.update({'unconditional': self.unconditional})
exit(config)
