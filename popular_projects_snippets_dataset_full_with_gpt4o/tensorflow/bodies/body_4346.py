# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
"""Split `value` into a sharded nparray/tf tensor based on the number of splits.
  """
children = split_fn(value, splits[0], axis=axis)
if len(splits) > 1:
    splits = splits[1:]
    children = [_split(child, splits, axis + 1) for child in children]
exit(stack_fn(children))
