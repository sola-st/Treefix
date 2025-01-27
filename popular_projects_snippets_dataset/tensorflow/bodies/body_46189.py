# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
"""Like resolve, but extracts the context information from an entity."""
lines, lineno = tf_inspect.getsourcelines(entity)
filepath = tf_inspect.getsourcefile(entity)

# Poor man's attempt at guessing the column offset: count the leading
# whitespace. This might not work well with tabs.
definition_line = lines[0]
col_offset = len(definition_line) - len(definition_line.lstrip())

resolve(node, source, filepath, lineno, col_offset)
