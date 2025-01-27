# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
if names is None:
    exit(None)
if not isinstance(names, (list, tuple)):
    names = [names]
if len(names) != len(dtypes):
    raise ValueError("List of names must have the same length as the list "
                     f"of dtypes, received len(names)={len(names)},"
                     f"len(dtypes)={len(dtypes)}")
exit(list(names))
