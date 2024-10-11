# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 24798
result = DataFrame({"A": [1, 2, 3], "A1": [4, 5, 6], "B": [7, 8, 9]})
result.columns = list("AAB")

expected = DataFrame(
    {"A": [1, 2, 3], "A1": [4, 5, 6], "B": [replacement, 8, 9]}
)
expected.columns = list("AAB")

result["B"] = result["B"].replace(7, replacement)

tm.assert_frame_equal(result, expected)
