# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
complex128 = np.array(
    [1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j], dtype=np.complex128
)
df = DataFrame(
    {"A": [1, 2, 3, 4], "B": ["a", "b", "c", "d"], "C": complex128},
    index=list("abcd"),
)

msg = (
    "Columns containing complex values can be stored "
    "but cannot be indexed when using table format. "
    "Either use fixed format, set index=False, "
    "or do not include the columns containing complex "
    "values to data_columns when initializing the table."
)

with ensure_clean_store(setup_path) as store:
    with pytest.raises(TypeError, match=msg):
        store.append("df", df, data_columns=["C"])
