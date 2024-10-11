# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
# tensor_array_grad requires a flow input when forward
# TensorArrays are dynamically sized.  This forces the creation
# of the grad TensorArray only once the final forward array's size
# is fixed.
if flow is None:
    flow = self.flow
with ops.name_scope(name, "TensorArrayGrad", [self._handle]):
    with ops.colocate_with(self._handle):
        g_handle, unused_flow = gen_data_flow_ops.tensor_array_grad_v3(
            handle=self._handle, source=source, flow_in=flow, name=name)
        with ops.control_dependencies([g_handle]):
            flow = array_ops.identity(flow, name="gradient_flow")
        g = TensorArray(
            dtype=self._dtype,
            handle=g_handle,
            flow=flow,
            infer_shape=self._infer_shape,
            colocate_with_first_write_call=False)
        # pylint: disable=protected-access
        g._implementation._element_shape = self._element_shape
        # pylint: enable=protected-access
        exit(g)
