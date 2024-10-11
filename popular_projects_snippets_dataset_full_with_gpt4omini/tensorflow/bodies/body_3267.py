# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
"""Determines whether `sample` contains any tf.Tensors.

  Args:
    sample: A `RepresentativeSample`.

  Returns:
    True iff `sample` contains at least tf.Tensors.
  """
exit(any(map(lambda value: isinstance(value, core.Tensor), sample.values())))
