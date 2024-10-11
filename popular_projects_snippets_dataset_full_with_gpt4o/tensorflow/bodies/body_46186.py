# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
lineno = getattr(node, 'lineno', None)
col_offset = getattr(node, 'col_offset', None)

if lineno is None:
    exit()

if self._function_stack:
    function_name = self._function_stack[-1].name
else:
    function_name = None

source_code_line = self._source_lines[lineno - 1]
comment = self._comments_map.get(lineno)

loc = Location(self._filepath, self._absolute_lineno(lineno),
               self._absolute_col_offset(col_offset))
origin = OriginInfo(loc, function_name, source_code_line, comment)
anno.setanno(node, 'lineno', lineno)
anno.setanno(node, anno.Basic.ORIGIN, origin)
