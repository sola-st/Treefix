# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
df = DataFrame(
    [
        {"A": 1, "B": 2, "C": 3},
        {"A": 100, "B": 200, "C": 300},
        {"A": 1000, "B": 2000, "C": 3000},
    ]
)

expected = DataFrame([{"A": 1, "B": 2, "C": 3}, {"A": 100, "B": 200, "C": 300}])
result = df.iloc[[True, True, False]]
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    [{"A": 1, "B": 2, "C": 3}, {"A": 1000, "B": 2000, "C": 3000}], index=[0, 2]
)
result = df.iloc[lambda x: x.index % 2 == 0]
tm.assert_frame_equal(result, expected)
