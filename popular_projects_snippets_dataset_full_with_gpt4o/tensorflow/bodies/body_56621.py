# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Dumps layer statistics into file, in csv format.

    Args:
      file: file, or file-like object to write.
    """
# order of `fields` is the order of fields in csv.
fields = ['op_name', 'tensor_idx'] + list(self._layer_debug_metrics.keys())
if self._debug_options.layer_direct_compare_metrics is not None:
    fields += list(self._debug_options.layer_direct_compare_metrics.keys())
fields += ['scale', 'zero_point', 'tensor_name']
writer = csv.DictWriter(file, fields)
writer.writeheader()
for name, metrics in self.layer_statistics.items():
    data = metrics.copy()
    (data['tensor_name'], _) = self._get_operand_name_and_index(name)
    data['tensor_idx'] = self._numeric_verify_op_details[name]['inputs'][0]
    data['op_name'] = self._quant_interpreter._get_op_details(  # pylint: disable=protected-access
        self._defining_op[data['tensor_idx']])['op_name']
    details = self._quant_interpreter._get_tensor_details(  # pylint: disable=protected-access
        data['tensor_idx'], subgraph_index=0)
    data['scale'], data['zero_point'] = (
        details['quantization_parameters']['scales'][0],
        details['quantization_parameters']['zero_points'][0])
    writer.writerow(data)
