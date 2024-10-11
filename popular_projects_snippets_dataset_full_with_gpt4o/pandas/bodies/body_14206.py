# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #26660
result = fmt.format_percentiles(np.linspace(0, 1, 10 + 1))
expected = [
    "0%",
    "10%",
    "20%",
    "30%",
    "40%",
    "50%",
    "60%",
    "70%",
    "80%",
    "90%",
    "100%",
]
assert result == expected
