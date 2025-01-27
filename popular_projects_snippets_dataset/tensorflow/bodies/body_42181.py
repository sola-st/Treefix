# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set a global eager mode seed for random ops."""
self._seed = seed
# `random.Random(seed)` needs `seed` to be hashable, while values of type
# e.g. `np.int64` or `np.ndarray` are not. We use `int(...)` to convert them
# to int.
try:
    hash(seed)
    self._rng = random.Random(seed)
except TypeError:
    seed = int(np.array(seed))
    self._rng = random.Random(seed)
# Also clear the kernel cache, to reset any existing seeds
if self._context_handle is not None:
    pywrap_tfe.TFE_ContextClearCaches(self._context_handle)
