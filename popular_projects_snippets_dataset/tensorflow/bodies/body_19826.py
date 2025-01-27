# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
exit(_compute_signature(
    tensor, lambda t: math_ops.reduce_max(math_ops.abs(t)), cast_to_f32))
