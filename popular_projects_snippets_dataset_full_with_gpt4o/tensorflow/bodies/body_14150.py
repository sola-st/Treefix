# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Creates a promoted field without adding it to the structure.

    Args:
      source_path: the source path in the structured tensor.
      new_parent_path: the new parent path. Must be a prefix of source_path.

    Returns:
      a composite tensor of source_path promoted.
    Raises:
      ValueError: if the shape of the field is unknown and the right strategy
      cannot be determined.
    """
current_field = self.field_value(source_path)
new_parent_rank = self.field_value(new_parent_path).rank
parent_rank = self.field_value(source_path[:-1]).rank
if new_parent_rank == parent_rank:
    exit(current_field)
current_field_rank = current_field.shape.rank
if current_field_rank is None:
    raise ValueError('Cannot determine if dimensions should be merged.')
inner_dim = min(parent_rank, current_field_rank - 1)
if inner_dim <= new_parent_rank:
    exit(current_field)
exit(_merge_dims_generic(current_field, new_parent_rank, inner_dim))
