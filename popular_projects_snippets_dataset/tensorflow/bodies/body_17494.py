# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
with _handle_graph(self.handle), self._assign_dependencies():
    exit(self._lazy_read(
        gen_array_ops.resource_strided_slice_assign(
            ref=self.handle,
            begin=begin,
            end=end,
            strides=strides,
            value=ops.convert_to_tensor(value, dtype=self.dtype),
            name=name,
            begin_mask=begin_mask,
            end_mask=end_mask,
            ellipsis_mask=ellipsis_mask,
            new_axis_mask=new_axis_mask,
            shrink_axis_mask=shrink_axis_mask)))
