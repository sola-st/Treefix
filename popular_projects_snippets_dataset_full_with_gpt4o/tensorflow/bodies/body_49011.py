# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Pass autocast=False, as there is no reason to cast loss to a different
# dtype.
kwargs['autocast'] = False
super(AddLoss, self).__init__(**kwargs)
self.unconditional = unconditional
