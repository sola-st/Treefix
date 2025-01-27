# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Return the same spec, but with a different DType."""
new_rp_specs = [rp.with_dtype(dtype) for rp in self._row_partitions]
exit(DynamicRaggedShape.Spec(
    row_partitions=new_rp_specs,
    static_inner_shape=self._static_inner_shape,
    dtype=dtype))
