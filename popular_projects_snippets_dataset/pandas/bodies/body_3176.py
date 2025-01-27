# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH 15891
# Normalize carriage return for Windows OS
result = (
    DataFrame([None, None])
    .to_csv(None, header=False, index=False, na_rep="")
    .replace("\r\n", "\n")
)
expected = '""\n""\n'
assert result == expected
