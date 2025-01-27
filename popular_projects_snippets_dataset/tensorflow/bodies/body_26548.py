# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""Maps `map_func` across the elements of this dataset.

  NOTE: This is a highly experimental version of `tf.data.Dataset.map` that runs
  `map_func` on GPU. It must be used after applying the
  `tf.data.experimental.copy_to_device` transformation with a GPU device
  argument.

  Args:
    map_func: A function mapping a nested structure of tensors (having shapes
      and types defined by `self.output_shapes` and `self.output_types`) to
      another nested structure of tensors.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    exit(_MapOnGpuDataset(dataset, map_func))

exit(_apply_fn)
