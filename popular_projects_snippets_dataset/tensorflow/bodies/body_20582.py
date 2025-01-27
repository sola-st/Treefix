# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Sets the number of shards for the current policy.

    If the policy has been frozen then number_of_shards must match the
    existing setting.

    Args:
      number_of_shards: The number of shards to use in the policy.

    Raises:
      ValueError: If the policy has been frozen and number_of_shards
        differs from the frozen value; or number_of_shards <= 0.
    """
if self._frozen:
    if self._number_of_shards != number_of_shards:
        raise ValueError(
            f"Can't set sharding policy to use {number_of_shards} shards since "
            f"it has been frozen to use {self._number_of_shards}")
else:
    if number_of_shards > 0:
        self._number_of_shards = number_of_shards
    else:
        raise ValueError(
            f"Can't set sharding policy to use {number_of_shards} shards; "
            "value must be > 0")
