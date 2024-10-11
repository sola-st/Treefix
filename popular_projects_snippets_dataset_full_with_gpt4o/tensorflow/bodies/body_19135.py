# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
r"""Asserts all items are of the same base type.

  Args:
    items: List of graph items (e.g., `Variable`, `Tensor`, `SparseTensor`,
        `Operation`, or `IndexedSlices`). Can include `None` elements, which
        will be ignored.
    expected_type: Expected type. If not specified, assert all items are
        of the same base type.

  Returns:
    Validated type, or none if neither expected_type nor items provided.

  Raises:
    ValueError: If any types do not match.
  """
original_expected_type = expected_type
mismatch = False
for item in items:
    if item is not None:
        item_type = item.dtype.base_dtype
        if not expected_type:
            expected_type = item_type
        elif expected_type != item_type:
            mismatch = True
            break
if mismatch:
    # Loop back through and build up an informative error message (this is very
    # slow, so we don't do it unless we found an error above).
    expected_type = original_expected_type
    original_item_str = None
    for item in items:
        if item is not None:
            item_type = item.dtype.base_dtype
            if not expected_type:
                expected_type = item_type
                original_item_str = item.name if hasattr(item, 'name') else str(item)
            elif expected_type != item_type:
                raise ValueError('%s, type=%s, must be of the same type (%s)%s.' % (
                    item.name if hasattr(item, 'name') else str(item),
                    item_type, expected_type,
                    (' as %s' % original_item_str) if original_item_str else ''))
    exit(expected_type)  # Should be unreachable
else:
    exit(expected_type)
