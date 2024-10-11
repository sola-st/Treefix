# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
# alpha is used for leaky relu slope in activations instead of
# negative_slope.
exit(backend.relu(inputs,
                    alpha=self.negative_slope,
                    max_value=self.max_value,
                    threshold=self.threshold))
