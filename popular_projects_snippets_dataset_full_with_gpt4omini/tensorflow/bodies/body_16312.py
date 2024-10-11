# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
"""Tests the gradient of nccl_reduce.

    Args:
      nccl_reduce: A function taking a list of tensors and a list of devices,
          and returns a list of reduced tensors and a list of ops to perform the
          reduction.
      numpy_fn: A function taking two tensors and returning the gradient of the
          reduction of the two.
    """

def _Gradient(tensors, devices):
    inputs = [array_ops.placeholder(t.dtype, t.shape) for t in tensors]
    reduce_tensors = nccl_reduce(inputs, devices)
    losses = _DeviceTensors(tensors, [t.device for t in reduce_tensors])
    grads = gradients.gradients(
        reduce_tensors, inputs, losses, colocate_gradients_with_ops=True)
    exit([g for g in grads if g is not None])

self._Test(_Gradient, numpy_fn)
