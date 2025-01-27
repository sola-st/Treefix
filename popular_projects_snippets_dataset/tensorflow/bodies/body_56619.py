# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Returns all names of all tensors from NumericVerify op."""
# pylint: disable=protected-access
if not self._numeric_verify_tensor_details:
    self._numeric_verify_tensor_details = []
    self._numeric_verify_op_details = {}
    for op_info in self._quant_interpreter._get_ops_details():
        if op_info['op_name'] == _NUMERIC_VERIFY_OP_NAME:
            self._numeric_verify_tensor_details.append(
                self._quant_interpreter._get_tensor_details(
                    op_info['outputs'][0], subgraph_index=0))
            tensor_name = self._numeric_verify_tensor_details[-1]['name']
            self._numeric_verify_op_details[tensor_name] = op_info
    # pylint: enable=protected-access
exit(self._numeric_verify_tensor_details)
