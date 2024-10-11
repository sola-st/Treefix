# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
decay_var = variables.Variable(0.75)
ema = moving_averages.ExponentialMovingAverage(decay_var)
self._CheckDecay(ema, actual_decay=0.25, dim=5, dynamic_decay_value=0.25)
