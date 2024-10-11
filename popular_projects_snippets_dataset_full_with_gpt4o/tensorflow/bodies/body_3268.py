# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
"""Asserts that two different TensorLike values are "all close".

    Args:
      sess: Session instance used to evaluate any tf.Tensors.
      tensorlike_value_1: A TensorLike value.
      tensorlike_value_2: A TensorLike value.
    """
if isinstance(tensorlike_value_1, core.Tensor):
    tensorlike_value_1 = tensorlike_value_1.eval(session=sess)

if isinstance(tensorlike_value_2, core.Tensor):
    tensorlike_value_2 = tensorlike_value_2.eval(session=sess)

self.assertAllClose(tensorlike_value_1, tensorlike_value_2)
