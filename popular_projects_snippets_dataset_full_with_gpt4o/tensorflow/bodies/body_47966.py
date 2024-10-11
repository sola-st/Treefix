# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
pos = backend.relu(inputs)
neg = -self.alpha * backend.relu(-inputs)
exit(pos + neg)
