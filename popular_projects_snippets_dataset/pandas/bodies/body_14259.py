# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 25608
df = DataFrame()
msg = "classes must be a string, list, or tuple"

with pytest.raises(TypeError, match=msg):
    df.to_html(classes=classes)
