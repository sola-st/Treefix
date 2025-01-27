# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if isinstance(x, slice):
    exit({'start': x.start, 'stop': x.stop, 'step': x.step})
exit(x)
