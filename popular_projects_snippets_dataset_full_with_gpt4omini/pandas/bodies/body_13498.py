# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# test with utf-8 and encoding option (GH 7061)
df = DataFrame([["au\xdfgangen"]])
with tm.ensure_clean("test.tex") as path:
    df.to_latex(path, encoding="utf-8")
    with codecs.open(path, "r", encoding="utf-8") as f:
        assert df.to_latex() == f.read()
