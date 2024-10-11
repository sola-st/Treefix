# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH 38581
df = DataFrame(
    {"col1": range(10, 20), "col2": range(20, 30), "colString": ["a"] * 10}
)
result = df.sample(3, ignore_index=True)
expected_index = Index(range(3))
tm.assert_index_equal(result.index, expected_index, exact=True)
