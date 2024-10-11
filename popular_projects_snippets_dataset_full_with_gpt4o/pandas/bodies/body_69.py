# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 35964
if op in ("ffill", "bfill", "pad", "backfill", "shift"):
    request.node.add_marker(
        pytest.mark.xfail(reason=f"{op} is successful on any dtype")
    )

# Using object makes most transform kernels fail
ser = Series(3 * [object])

if op in ("fillna", "ngroup"):
    error = ValueError
    msg = "Transform function failed"
else:
    error = TypeError
    msg = "|".join(
        [
            "not supported between instances of 'type' and 'type'",
            "unsupported operand type",
        ]
    )

with pytest.raises(error, match=msg):
    ser.transform([op, "shift"])

with pytest.raises(error, match=msg):
    ser.transform({"A": op, "B": "shift"})

with pytest.raises(error, match=msg):
    ser.transform({"A": [op], "B": ["shift"]})

with pytest.raises(error, match=msg):
    ser.transform({"A": [op, "shift"], "B": [op]})
