# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
ema = moving_averages.ExponentialMovingAverage(0.25)
self._CheckDecay(ema, actual_decay=0.25, dim=1)
