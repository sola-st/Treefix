# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
df = DataFrame([[9]])
with option_context("styler.format.formatter", formatter):
    assert f" {exp} " in df.style.to_latex()
