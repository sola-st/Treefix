# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("display.expand_frame_repr", False):
    df = DataFrame(index=index(h), columns=tm.makeStringIndex(w))
    with option_context("display.max_rows", 15):
        if h == 20:
            assert has_vertically_truncated_repr(df)
        else:
            assert not has_vertically_truncated_repr(df)
    with option_context("display.max_columns", 15):
        if w == 20:
            assert has_horizontally_truncated_repr(df)
        else:
            assert not has_horizontally_truncated_repr(df)
    with option_context("display.max_rows", 15, "display.max_columns", 15):
        if h == 20 and w == 20:
            assert has_doubly_truncated_repr(df)
        else:
            assert not has_doubly_truncated_repr(df)
