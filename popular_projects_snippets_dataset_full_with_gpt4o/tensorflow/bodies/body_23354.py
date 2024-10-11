# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Prints a row."""
line = ""
for i, field in enumerate(fields):
    field = str(field)
    end_line_pos = positions[i]
    if i > 0:
        line = line + " "
    line = "{0:{min_length}}".format(line + field, min_length=end_line_pos)

    if len(line) > end_line_pos:
        line = line[:(end_line_pos - 4)] + " ..."

print_fn(line)
