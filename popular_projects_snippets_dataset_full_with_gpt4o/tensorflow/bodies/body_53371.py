# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
a = self._numpy()
if not dtype:
    exit(a)

exit(np.array(a, dtype=dtype))
