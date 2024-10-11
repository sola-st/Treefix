# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
msg = "|".join(
    [
        r"index 101 is out of bounds for axis 0 with size [\d]+",
        re.escape(
            "only integers, slices (`:`), ellipsis (`...`), "
            "numpy.newaxis (`None`) and integer or boolean arrays "
            "are valid indices"
        ),
        "index out of bounds",  # string[pyarrow]
    ]
)
with pytest.raises(IndexError, match=msg):
    index[item]
