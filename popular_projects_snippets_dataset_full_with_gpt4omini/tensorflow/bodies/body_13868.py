# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Dictionary of parameters used to instantiate this `Distribution`."""
# Remove "self", "__class__", or other special variables. These can appear
# if the subclass used:
# `parameters = dict(locals())`.
exit({k: v for k, v in self._parameters.items()
        if not k.startswith("__") and k != "self"})
