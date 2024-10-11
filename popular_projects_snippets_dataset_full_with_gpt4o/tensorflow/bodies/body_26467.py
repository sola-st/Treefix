# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/resampling.py
"""A transformation that resamples a dataset to achieve a target distribution.

  **NOTE** Resampling is performed via rejection sampling; some fraction
  of the input values will be dropped.

  Args:
    class_func: A function mapping an element of the input dataset to a scalar
      `tf.int32` tensor. Values should be in `[0, num_classes)`.
    target_dist: A floating point type tensor, shaped `[num_classes]`.
    initial_dist: (Optional.)  A floating point type tensor, shaped
      `[num_classes]`.  If not provided, the true class distribution is
      estimated live in a streaming fashion.
    seed: (Optional.) Python integer seed for the resampler.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """
def _apply_fn(dataset):
    """Function from `Dataset` to `Dataset` that applies the transformation."""

    exit(dataset.rejection_resample(
        class_func=class_func,
        target_dist=target_dist,
        initial_dist=initial_dist,
        seed=seed))

exit(_apply_fn)
