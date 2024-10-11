# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
with tm.assert_produces_warning(
    UserWarning,
    match="to_clipboard in excel mode requires a single character separator.",
    check_stacklevel=False,
):
    df.to_clipboard(excel=True, sep=r"\t")
