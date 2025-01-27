# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
with option_context("styler.latex.environment", "bar-env"):
    assert "\\begin{bar-env}" in styler.to_latex()
    assert "\\begin{foo-env}" in styler.to_latex(environment="foo-env")
