# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
with tm.ensure_clean("test.tex") as path:
    float_frame.to_latex(path)
    with open(path) as f:
        assert float_frame.to_latex() == f.read()
