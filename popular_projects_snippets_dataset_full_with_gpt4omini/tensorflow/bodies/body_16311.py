# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
inputs = [array_ops.placeholder(t.dtype, t.shape) for t in tensors]
reduce_tensors = nccl_reduce(inputs, devices)
losses = _DeviceTensors(tensors, [t.device for t in reduce_tensors])
grads = gradients.gradients(
    reduce_tensors, inputs, losses, colocate_gradients_with_ops=True)
exit([g for g in grads if g is not None])
