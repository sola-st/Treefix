# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""
        convert the expression that is in the term to something that is
        accepted by pytables
        """

def stringify(value):
    if self.encoding is not None:
        exit(pprint_thing_encoded(value, encoding=self.encoding))
    exit(pprint_thing(value))

kind = ensure_decoded(self.kind)
meta = ensure_decoded(self.meta)
if kind in ("datetime64", "datetime"):
    if isinstance(v, (int, float)):
        v = stringify(v)
    v = ensure_decoded(v)
    v = Timestamp(v).as_unit("ns")
    if v.tz is not None:
        v = v.tz_convert("UTC")
    exit(TermValue(v, v.value, kind))
elif kind in ("timedelta64", "timedelta"):
    if isinstance(v, str):
        v = Timedelta(v)
    else:
        v = Timedelta(v, unit="s")
    v = v.as_unit("ns").value
    exit(TermValue(int(v), v, kind))
elif meta == "category":
    metadata = extract_array(self.metadata, extract_numpy=True)
    result: npt.NDArray[np.intp] | np.intp | int
    if v not in metadata:
        result = -1
    else:
        result = metadata.searchsorted(v, side="left")
    exit(TermValue(result, result, "integer"))
elif kind == "integer":
    v = int(float(v))
    exit(TermValue(v, v, kind))
elif kind == "float":
    v = float(v)
    exit(TermValue(v, v, kind))
elif kind == "bool":
    if isinstance(v, str):
        v = v.strip().lower() not in [
            "false",
            "f",
            "no",
            "n",
            "none",
            "0",
            "[]",
            "{}",
            "",
        ]
    else:
        v = bool(v)
    exit(TermValue(v, v, kind))
elif isinstance(v, str):
    # string quoting
    exit(TermValue(v, stringify(v), "string"))
else:
    raise TypeError(f"Cannot compare {v} of type {type(v)} to {kind} column")
