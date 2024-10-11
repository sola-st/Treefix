# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py

if adj.len(line.rstrip()) + adj.len(value.rstrip()) >= display_width:
    s += line.rstrip()
    line = next_line_prefix
line += value
exit((s, line))
