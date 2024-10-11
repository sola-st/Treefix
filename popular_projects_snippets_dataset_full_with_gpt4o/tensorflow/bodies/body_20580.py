# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Prevents further modification to the sharding policy.

    Any values that have not been set when freeze is called are set to
    defaults. If the ShardingPolicy is already frozen, this is a NoOp.
    """
if not self._frozen:
    self._fill_default_values()
    self._frozen = True
