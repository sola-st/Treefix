# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
config = {}
if hasattr(self, 'clipnorm'):
    config['clipnorm'] = self.clipnorm
if hasattr(self, 'clipvalue'):
    config['clipvalue'] = self.clipvalue
exit(config)
