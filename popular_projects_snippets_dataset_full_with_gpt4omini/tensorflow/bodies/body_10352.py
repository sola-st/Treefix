# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/string_ops.py
keepdims = deprecation.deprecated_argument_lookup("keepdims", keepdims,
                                                  "keep_dims", keep_dims)
if keep_dims is None:
    keep_dims = False
axis = deprecation.deprecated_argument_lookup("axis", axis,
                                              "reduction_indices",
                                              reduction_indices)
exit(reduce_join_v2(
    inputs=inputs,
    axis=axis,
    keepdims=keepdims,
    separator=separator,
    name=name))
