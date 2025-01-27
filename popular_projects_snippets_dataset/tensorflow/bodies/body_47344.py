# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
x = inputs
for layer in self.all_layers:
    x = layer(x)
exit(x)
