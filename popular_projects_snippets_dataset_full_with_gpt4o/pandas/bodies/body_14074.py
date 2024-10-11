# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("mode.sim_interactive", True, "display.max_columns", 20):
    max_cols = get_option("display.max_columns")
    midx = MultiIndex.from_arrays(tm.rands_array(5, size=(2, 10)))
    mcols = MultiIndex.from_arrays(tm.rands_array(3, size=(2, max_cols - 1)))
    df = DataFrame(
        tm.rands_array(25, (10, max_cols - 1)), index=midx, columns=mcols
    )
    df.index.names = ["Level 0", "Level 1"]
    with option_context("display.expand_frame_repr", False):
        rep_str = repr(df)
    with option_context("display.expand_frame_repr", True):
        wide_repr = repr(df)
    assert rep_str != wide_repr

with option_context("display.width", 150, "display.max_columns", 20):
    wider_repr = repr(df)
    assert len(wider_repr) < len(wide_repr)
