# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Estimate data distribution as labels are seen.

  Args:
    c: The class labels.  Type `int32`, shape `[batch_size]`.
    num_examples_per_class_seen: Type `int64`, shape `[num_classes]`, containing
      counts.

  Returns:
    num_examples_per_lass_seen: Updated counts.  Type `int64`, shape
      `[num_classes]`.
    dist: The updated distribution.  Type `float32`, shape `[num_classes]`.
  """
num_classes = num_examples_per_class_seen.get_shape()[0]
# Update the class-count based on what labels are seen in batch.
num_examples_per_class_seen = math_ops.add(
    num_examples_per_class_seen,
    math_ops.reduce_sum(
        array_ops.one_hot(c, num_classes, dtype=dtypes.int64), 0))
init_prob_estimate = math_ops.truediv(
    num_examples_per_class_seen,
    math_ops.reduce_sum(num_examples_per_class_seen))
dist = math_ops.cast(init_prob_estimate, dtypes.float32)
exit((num_examples_per_class_seen, dist))
