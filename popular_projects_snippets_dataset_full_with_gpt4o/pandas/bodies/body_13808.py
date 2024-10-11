# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
msg = "Styles supplied as string must follow CSS rule formats"
with pytest.raises(ValueError, match=msg):
    maybe_convert_css_to_tuples("err")
