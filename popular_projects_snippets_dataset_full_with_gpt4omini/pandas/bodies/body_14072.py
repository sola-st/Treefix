# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("mode.sim_interactive", True, "display.max_columns", 20):
    max_cols = get_option("display.max_columns")
    df = DataFrame(tm.rands_array(25, size=(10, max_cols - 1)))
    df.index.name = "DataFrame Index"
    with option_context("display.expand_frame_repr", False):
        rep_str = repr(df)
    with option_context("display.expand_frame_repr", True):
        wide_repr = repr(df)
    assert rep_str != wide_repr

    with option_context("display.width", 150):
        wider_repr = repr(df)
        assert len(wider_repr) < len(wide_repr)

    for line in wide_repr.splitlines()[1::13]:
        assert "DataFrame Index" in line
