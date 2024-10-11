# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
msg = "Value must be an instance of"
with pytest.raises(ValueError, match=msg):
    with option_context("styler.format.formatter", ["bad", "type"]):
        DataFrame().style.to_latex()
