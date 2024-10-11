# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
with pytest.raises(ValueError, match="No axis named bad for object type DataFrame"):
    styler.set_sticky(axis="bad")
