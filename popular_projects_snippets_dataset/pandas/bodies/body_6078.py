# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# TODO: box over scalar, [scalar], (scalar,)?

msg = (
    r"only integers, slices \(`:`\), ellipsis \(`...`\), numpy.newaxis "
    r"\(`None`\) and integer or boolean arrays are valid indices"
)
with pytest.raises(IndexError, match=msg):
    data["foo"]
with pytest.raises(IndexError, match=msg):
    data[2.5]

ub = len(data)
msg = "|".join(
    [
        "list index out of range",  # json
        "index out of bounds",  # pyarrow
        "Out of bounds access",  # Sparse
        f"loc must be an integer between -{ub} and {ub}",  # Sparse
        f"index {ub+1} is out of bounds for axis 0 with size {ub}",
        f"index -{ub+1} is out of bounds for axis 0 with size {ub}",
    ]
)
with pytest.raises(IndexError, match=msg):
    data[ub + 1]
with pytest.raises(IndexError, match=msg):
    data[-ub - 1]
