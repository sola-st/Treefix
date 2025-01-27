# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df_small = DataFrame("hello", index=[0], columns=[0])
df_wide = DataFrame("hello", index=[0], columns=range(10))
df_tall = DataFrame("hello", index=range(30), columns=range(5))

with option_context("mode.sim_interactive", True):
    with option_context(
        "display.max_columns",
        10,
        "display.width",
        20,
        "display.max_rows",
        20,
        "display.show_dimensions",
        True,
    ):
        with option_context("display.expand_frame_repr", True):
            assert not has_truncated_repr(df_small)
            assert not has_expanded_repr(df_small)
            assert not has_truncated_repr(df_wide)
            assert has_expanded_repr(df_wide)
            assert has_vertically_truncated_repr(df_tall)
            assert has_expanded_repr(df_tall)

        with option_context("display.expand_frame_repr", False):
            assert not has_truncated_repr(df_small)
            assert not has_expanded_repr(df_small)
            assert not has_horizontally_truncated_repr(df_wide)
            assert not has_expanded_repr(df_wide)
            assert has_vertically_truncated_repr(df_tall)
            assert not has_expanded_repr(df_tall)
