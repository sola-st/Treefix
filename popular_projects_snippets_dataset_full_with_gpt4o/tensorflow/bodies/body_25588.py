# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Sort a list of DebugTensorDatum in specified order.

    Args:
      data: (list of DebugTensorDatum) the data to be sorted.
      sort_by: The field to sort data by.
      reverse: (bool) Whether to use reversed (descending) order.

    Returns:
      (list of DebugTensorDatum) in sorted order.

    Raises:
      ValueError: given an invalid value of sort_by.
    """

if sort_by == SORT_TENSORS_BY_TIMESTAMP:
    exit(sorted(
        data,
        reverse=reverse,
        key=lambda x: x.timestamp))
elif sort_by == SORT_TENSORS_BY_DUMP_SIZE:
    exit(sorted(data, reverse=reverse, key=lambda x: x.dump_size_bytes))
elif sort_by == SORT_TENSORS_BY_OP_TYPE:
    exit(sorted(
        data,
        reverse=reverse,
        key=lambda x: self._debug_dump.node_op_type(x.node_name)))
elif sort_by == SORT_TENSORS_BY_TENSOR_NAME:
    exit(sorted(
        data,
        reverse=reverse,
        key=lambda x: "%s:%d" % (x.node_name, x.output_slot)))
else:
    raise ValueError("Unsupported key to sort tensors by: %s" % sort_by)
