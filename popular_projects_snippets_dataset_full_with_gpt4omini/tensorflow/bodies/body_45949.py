# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns a clean node and source code without indenting and context."""
for n in gast.walk(node):
    lineno = getattr(n, 'lineno', None)
    if lineno is not None:
        n.lineno = lineno - minl
    end_lineno = getattr(n, 'end_lineno', None)
    if end_lineno is not None:
        n.end_lineno = end_lineno - minl

code_lines = lines[minl - 1:maxl]

# Attempt to clean up surrounding context code.

end_col_offset = getattr(node, 'end_col_offset', None)
if end_col_offset is not None:
    # This is only available in 3.8.
    code_lines[-1] = code_lines[-1][:end_col_offset]

col_offset = getattr(node, 'col_offset', None)
if col_offset is None:
    # Older Python: try to find the "lambda" token. This is brittle.
    match = re.search(r'(?<!\w)lambda(?!\w)', code_lines[0])
    if match is not None:
        col_offset = match.start(0)

if col_offset is not None:
    code_lines[0] = code_lines[0][col_offset:]

code_block = '\n'.join([c.rstrip() for c in code_lines])

exit((node, code_block))
