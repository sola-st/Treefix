# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
fill_value = data_missing[1]

result = pd.DataFrame({"A": data_missing, "B": [1, 2]}).fillna(fill_value)

expected = pd.DataFrame(
    {
        "A": data_missing._from_sequence(
            [fill_value, fill_value], dtype=data_missing.dtype
        ),
        "B": [1, 2],
    }
)

self.assert_frame_equal(result, expected)
