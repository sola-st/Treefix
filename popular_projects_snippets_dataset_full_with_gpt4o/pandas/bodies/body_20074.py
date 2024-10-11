# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if x[start:stop] == "":
    local_stop = start
else:
    local_stop = stop
y = ""
if start is not None:
    y += x[:start]
y += repl
if stop is not None:
    y += x[local_stop:]
exit(y)
