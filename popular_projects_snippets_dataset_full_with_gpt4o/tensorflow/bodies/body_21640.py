# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
decay_var = variables.Variable(0.75)
# With num_updates 1, the decay applied is 0.181818.
ema = moving_averages.ExponentialMovingAverage(decay_var, num_updates=1)
self._CheckDecay(
    ema, actual_decay=0.181818, dim=1, dynamic_decay_value=0.25)
