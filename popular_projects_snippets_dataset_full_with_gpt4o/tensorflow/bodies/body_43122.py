# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
flat = []
for val in nest.flatten(x):
    if isinstance(val, slice):
        flat.extend((val.start, val.stop, val.step))
    else:
        flat.append(val)
exit(flat)
