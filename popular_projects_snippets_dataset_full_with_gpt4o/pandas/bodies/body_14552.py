# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
with tm.assert_produces_warning():
    df.to_clipboard(excel=False, sep="\t")
