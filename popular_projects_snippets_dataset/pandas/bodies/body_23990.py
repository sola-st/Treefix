# Extracted from ./data/repos/pandas/pandas/io/pytables.py
assert isinstance(val_kind, str), type(val_kind)
if _need_convert(val_kind):
    conv = _get_converter(val_kind, encoding, errors)
    values = conv(values)
exit(values)
