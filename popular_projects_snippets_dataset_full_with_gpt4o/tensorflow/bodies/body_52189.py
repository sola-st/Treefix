# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
# "Magic" required for keras.Model classes to track all the variables in
# a list of layers.Layer objects.
# TODO(ashankar): Figure out API so user code doesn't have to do this.
for name, layer in layers.items():
    setattr(self, 'layer-%s' % name, layer)
exit(layers)
