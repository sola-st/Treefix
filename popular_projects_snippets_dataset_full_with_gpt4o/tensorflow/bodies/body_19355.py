# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the Op-list section of the report."""

self._write_report('%s %s\n'%(_MARKER_SECTION_BEGIN, _SECTION_NAME_OP_LIST))
self._write_report('%s %d\n'%(_FIELD_NAME_NUM_OPS,
                              len(graph_order.operations)))
for i in range(0, len(graph_order.operations)):
    op = graph_order.operations[i]
    line = '%d "%s" %s'%(i, op.name, op.type)
    for out_tensor in op.outputs:
        if out_tensor.name not in graph_order.tensor_to_idx:
            raise ValueError(
                'out_tensor is not in tensor_to_idx. out_tensor={}, '
                'tensor_to_idx={}'
                .format(out_tensor.name, graph_order.tensor_to_idx))
        line += ' %d'%graph_order.tensor_to_idx[out_tensor.name]
    line += '\n'
    self._write_report(line)
self._write_report('%s %s\n'%(_MARKER_SECTION_END, _SECTION_NAME_OP_LIST))
