# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
if zero_debias:
    exit(_zero_debias(strategy, v, value, decay))
else:
    exit(_update(strategy, v, update_fn, args=(value,)))
