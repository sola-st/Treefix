# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH36189
pdf = DataFrame([[4, 9]] * 3, columns=["A", "B"])
result = pdf.apply(["sum", lambda x: x.sum(), lambda x: x.sum()])
expected = DataFrame(
    {"A": [12, 12, 12], "B": [27, 27, 27]}, index=["sum", "<lambda>", "<lambda>"]
)

tm.assert_frame_equal(result, expected)
