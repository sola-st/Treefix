# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
exit(math_ops.logical_and(
    math_ops.reduce_min(output_size) < max_output_size,
    idx < num_iterations))
