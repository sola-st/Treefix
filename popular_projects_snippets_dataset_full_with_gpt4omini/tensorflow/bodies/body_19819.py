# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
# In order to check the size of a tensor.
# Not all sizes are known at the compile time, also, different replicas
# sometimes get different sizes of tensors.
# Collect it here to be used in merging replica data.
tsize = _compute_signature(tensor, array_ops.size, cast_to_f32=False)
# Cast to float32, so that it can be placed into same cache with other
# signatures.
exit(math_ops.cast(tsize, dtypes.float32))
