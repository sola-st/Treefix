# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH#40024
df = DataFrame(data={"x": [1000.0, "test"]})
result = df.to_html(float_format=lambda x: f"{x:,.0f}")
expected = expected_html(datapath, "gh40024_expected_output")
assert result == expected
