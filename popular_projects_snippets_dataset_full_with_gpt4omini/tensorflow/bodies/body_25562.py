# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Get the content of a cell of the table.

    Args:
      row: (int) row index.
      col: (int) column index.
      device_name_filter: Regular expression to filter by device name.
      node_name_filter: Regular expression to filter by node name.
      op_type_filter: Regular expression to filter by op type.

    Returns:
      A debuggre_cli_common.RichLine object representing the content of the
      cell, potentially with a clickable MenuItem.

    Raises:
      IndexError: if row index is out of range.
    """
menu_item = None
if col == 0:
    text = self._profile_datum_list[row].node_exec_stats.node_name
elif col == 1:
    text = self._profile_datum_list[row].op_type
elif col == 2:
    text = str(self.formatted_start_time[row])
elif col == 3:
    text = str(self.formatted_op_time[row])
elif col == 4:
    text = str(self.formatted_exec_time[row])
elif col == 5:
    command = "ps"
    if device_name_filter:
        command += " --%s %s" % (_DEVICE_NAME_FILTER_FLAG,
                                 device_name_filter)
    if node_name_filter:
        command += " --%s %s" % (_NODE_NAME_FILTER_FLAG, node_name_filter)
    if op_type_filter:
        command += " --%s %s" % (_OP_TYPE_FILTER_FLAG, op_type_filter)
    command += " %s --init_line %d" % (
        self._profile_datum_list[row].file_path,
        self._profile_datum_list[row].line_number)
    menu_item = debugger_cli_common.MenuItem(None, command)
    text = self._profile_datum_list[row].file_line_func
else:
    raise IndexError("Invalid column index %d." % col)

exit(RL(text, font_attr=menu_item))
