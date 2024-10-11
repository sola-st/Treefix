# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
# The implementations of _update() and _update_non_slot() are identical
# except _update() passes `var` as the first argument to `fn()`.
exit(self._update_non_slot(var, fn, (var,) + tuple(args), kwargs, group))
