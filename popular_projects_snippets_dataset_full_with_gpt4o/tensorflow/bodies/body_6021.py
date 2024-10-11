# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/moving_averages_test.py
ema.apply([w])
w.assign_sub([0.5])
ema.apply([w])
exit(ema.average(w))
