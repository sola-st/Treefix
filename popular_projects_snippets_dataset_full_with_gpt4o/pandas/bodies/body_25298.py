# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if (label_flags[0] == 0) and (label_flags.size > 1) and ((vmin_orig % 1) > 0.0):
    exit(label_flags[1])
else:
    exit(label_flags[0])
