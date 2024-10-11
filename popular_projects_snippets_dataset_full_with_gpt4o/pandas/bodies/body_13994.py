# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
with tm.assert_produces_warning(CSSWarning):
    assert_same_resolution(invalid_css, remainder)
