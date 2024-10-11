# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
self._source_lines = source_lines
self._comments_map = comments_map

if (hasattr(root_node, 'decorator_list') and root_node.decorator_list and
    hasattr(root_node.decorator_list[0], 'lineno')):
    # Typical case: functions. The line number of the first decorator
    # is more accurate than the line number of the function itself in
    # 3.8+. In earier versions they coincide.
    self._lineno_offset = context_lineno - root_node.decorator_list[0].lineno
else:
    # Fall back to the line number of the root node.
    self._lineno_offset = context_lineno - root_node.lineno

self._col_offset = context_col_offset - root_node.col_offset

self._filepath = filepath

self._function_stack = []
