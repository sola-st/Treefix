# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Returns a dict mapping arg_name to DeprecatedArgSpec w/o position."""
d = {}
for name_or_tuple in deprecated_arg_names_or_tuples:
    if isinstance(name_or_tuple, tuple):
        d[name_or_tuple[0]] = DeprecatedArgSpec(-1, True, name_or_tuple[1])
    else:
        d[name_or_tuple] = DeprecatedArgSpec(-1, False, None)
exit(d)
