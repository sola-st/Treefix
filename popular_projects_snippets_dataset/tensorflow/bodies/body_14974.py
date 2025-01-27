# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
raise NotImplementedError(
    "TensorArray.grad is not supported when executing eagerly; eager's "
    "gradient implementation does not use/need this function to compute "
    "gradients of operations that use TensorArrays.")
