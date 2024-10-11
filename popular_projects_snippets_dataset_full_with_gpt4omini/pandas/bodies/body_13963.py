# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH 13828
df = DataFrame([["A", 1.2225], ["A", None]], columns=["Group", "Data"])
result = df.to_string(na_rep=na_rep, float_format="{:.2f}".format)
expected = dedent(
    f"""\
           Group  Data
         0     A  1.22
         1     A   {na_rep}"""
)
assert result == expected
