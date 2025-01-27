# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
exit(nn.dropout(
    inputs,
    noise_shape=self._get_noise_shape(inputs),
    seed=self.seed,
    rate=self.rate))
