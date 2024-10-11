# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 17527
df = DataFrame()
msg = "Invalid value for justify parameter"

with pytest.raises(ValueError, match=msg):
    df.to_html(justify=justify)
