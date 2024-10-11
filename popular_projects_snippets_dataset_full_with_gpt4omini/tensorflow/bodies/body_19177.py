# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Validates the features in this ParseOpParams."""
if len(self.dense_shapes) != len(self.dense_keys):
    raise ValueError("len(self.dense_shapes) != len(self.dense_keys): "
                     f"{len(self.dense_shapes)} vs {len(self.dense_keys)}.")
if len(self.dense_types) != len(self.dense_keys):
    raise ValueError("len(self.dense_types) != len(self.dense_keys): "
                     f"{len(self.dense_types)} vs {len(self.dense_keys)}.")
if len(self.sparse_types) != len(self.sparse_keys):
    raise ValueError("len(self.sparse_types) != len(self.sparse_keys): "
                     f"{len(self.sparse_types)} vs {len(self.sparse_keys)}.")
if len(self.ragged_value_types) != len(self.ragged_keys):
    raise ValueError(
        "len(self.ragged_value_types) != len(self.ragged_keys): "
        f"{len(self.ragged_value_types)} vs {len(self.ragged_keys)}.")
if len(self.ragged_split_types) != len(self.ragged_keys):
    raise ValueError(
        "len(self.ragged_split_types) != len(self.ragged_keys): "
        f"{len(self.ragged_split_types)} vs {len(self.ragged_keys)}.")

dense_key_set = set(self.dense_keys)
sparse_key_set = set(self.sparse_keys)
ragged_key_set = set(self.ragged_keys)
if not dense_key_set.isdisjoint(sparse_key_set):
    raise ValueError(
        "Dense and sparse keys must not intersect; dense_keys: "
        f"{self.dense_keys}, sparse_keys: {self.sparse_keys}, intersection: "
        f"{dense_key_set.intersection(sparse_key_set)}")
if not dense_key_set.isdisjoint(ragged_key_set):
    raise ValueError(
        "Dense and ragged keys must not intersect; dense_keys: ",
        f"{self.dense_keys}, ragged_keys: {self.ragged_keys}, intersection: "
        f"{dense_key_set.intersection(ragged_key_set)}")
if not ragged_key_set.isdisjoint(sparse_key_set):
    raise ValueError(
        "Ragged and sparse keys must not intersect; ragged_keys: "
        f"{self.ragged_keys}, sparse_keys: {self.sparse_keys}, intersection: "
        f"{ragged_key_set.intersection(sparse_key_set)}")
