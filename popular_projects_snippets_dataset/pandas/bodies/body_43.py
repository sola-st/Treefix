# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 35964

if op == "ngroup":
    request.node.add_marker(
        pytest.mark.xfail(raises=ValueError, reason="ngroup not valid for NDFrame")
    )

# Using object makes most transform kernels fail
df = DataFrame({"A": 3 * [object], "B": [1, 2, 3]})
error = TypeError
msg = "|".join(
    [
        "not supported between instances of 'type' and 'type'",
        "unsupported operand type",
    ]
)

with pytest.raises(error, match=msg):
    df.transform([op])

with pytest.raises(error, match=msg):
    df.transform({"A": op, "B": op})

with pytest.raises(error, match=msg):
    df.transform({"A": [op], "B": [op]})

with pytest.raises(error, match=msg):
    df.transform({"A": [op, "shift"], "B": [op]})
