# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 21527 28358
df = DataFrame([[None, None], [1.1, 1.2]], columns=["A", "B"])

ctx = Styler(df, na_rep="NA")._translate(True, True)
assert ctx["body"][0][1]["display_value"] == "NA"
assert ctx["body"][0][2]["display_value"] == "NA"
