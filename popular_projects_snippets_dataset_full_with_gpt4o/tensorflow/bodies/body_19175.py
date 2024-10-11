# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a ragged key & dtype, checking for duplicates."""
if key in self.ragged_keys:
    original_value_type = self.ragged_value_types[self.ragged_keys.index(key)]
    original_split_type = self.ragged_split_types[self.ragged_keys.index(key)]
    if original_value_type != value_type:
        raise ValueError(f"Conflicting type {original_value_type} vs "
                         f"{value_type} for feature {key}.")
    if original_split_type != split_type:
        raise ValueError(f"Conflicting partition type {original_split_type} vs "
                         f"{split_type} for feature {key}.")
else:
    self.ragged_keys.append(key)
    self.ragged_value_types.append(value_type)
    self.ragged_split_types.append(split_type)
