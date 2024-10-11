# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/take_while_ops.py
"""A transformation that stops dataset iteration based on a `predicate`.

  Args:
    predicate: A function that maps a nested structure of tensors (having shapes
      and types defined by `self.output_shapes` and `self.output_types`) to a
      scalar `tf.bool` tensor.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    exit(dataset.take_while(predicate=predicate))

exit(_apply_fn)
