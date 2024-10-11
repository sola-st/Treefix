# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
with option_context("styler.render.encoding", "ASCII"):
    result = styler.to_html(doctype_html=True)
    assert '<meta charset="ASCII">' in result
    result = styler.to_html(doctype_html=True, encoding="ANSI")
    assert '<meta charset="ANSI">' in result
