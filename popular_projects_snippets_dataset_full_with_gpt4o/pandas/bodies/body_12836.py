# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH 35849
# Test ValueError when mode is not supported option
df = DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
msg = (
    f"mode={mode_} is not a valid option."
    "Only 'w' and 'a' are currently supported."
)
with pytest.raises(ValueError, match=msg):
    df.to_json(mode=mode_, lines=False, orient="records")
