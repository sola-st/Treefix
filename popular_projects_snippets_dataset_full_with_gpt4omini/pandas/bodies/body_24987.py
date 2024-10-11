# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
assert float_format is not None  # for mypy
# error: "str" not callable
# error: Unexpected keyword argument "value" for "__call__" of
# "EngFormatter"
exit((
    float_format(value=v)  # type: ignore[operator,call-arg]
    if notna(v)
    else self.na_rep
))
