# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Calculate output shape for vectorized loop. This will be used as
# shape_invariant. Merges shape inference outputs with the `output_shapes`
# attribute of the op.
output_shapes = [out.shape for out in self._pfor_input.op.outputs]
shapes = self._pfor_input.get_attr("output_shapes")
if not shapes:
    shapes = [tensor_shape.TensorShape(None) for _ in output_shapes]
else:
    shapes = [tensor_shape.TensorShape(shape) for shape in shapes]
for i, shape in enumerate(shapes):
    shape = shape.merge_with(output_shapes[i])
    pfor_input = self._pfor_input.input(i)
    if pfor_input.is_stacked:
        if _is_variant_with_internal_stacking(pfor_input.t):
            shape = tensor_shape.TensorShape([]).concatenate(shape)
        else:
            shape = tensor_shape.TensorShape([None]).concatenate(shape)
    output_shapes[i] = shape
assert len(output_shapes) == self._pfor_input.num_inputs
exit(output_shapes)
