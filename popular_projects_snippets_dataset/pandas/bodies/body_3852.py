# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# only an issue with long columns
df3 = DataFrame(
    {
        "A" * 30: {("A", "A0006000", "nuit"): "A0006000"},
        "B" * 30: {("A", "A0006000", "nuit"): np.nan},
        "C" * 30: {("A", "A0006000", "nuit"): np.nan},
        "D" * 30: {("A", "A0006000", "nuit"): np.nan},
        "E" * 30: {("A", "A0006000", "nuit"): "A"},
        "F" * 30: {("A", "A0006000", "nuit"): np.nan},
    }
)

idf = df3.set_index(["A" * 30, "C" * 30])
repr(idf)
