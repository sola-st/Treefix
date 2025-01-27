# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
x = inputs
for i in range(self.num_layers):
    layer = getattr(self, self._layer_name_for_i(i))
    x = layer(x)
exit(x)
