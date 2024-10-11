# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
exit(tensor_array_ops.TensorArray(
    dtype=elem.dtype, size=n, dynamic_size=False,
    infer_shape=True).unstack(elem))
