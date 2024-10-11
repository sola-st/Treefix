# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
term_width, term_height = get_terminal_size()
fac = 1.05  # Arbitrary large factor to exceed term width
cols = range(int(term_width * fac))
index = range(10)
df = DataFrame(index=index, columns=cols)
with option_context("mode.sim_interactive", True):
    with option_context("display.max_rows", None):
        with option_context("display.max_columns", None):
            # Wrap around with None
            assert has_expanded_repr(df)
    with option_context("display.max_rows", 0):
        with option_context("display.max_columns", 0):
            # Truncate with auto detection.
            assert has_horizontally_truncated_repr(df)

    index = range(int(term_height * fac))
    df = DataFrame(index=index, columns=cols)
    with option_context("display.max_rows", 0):
        with option_context("display.max_columns", None):
            # Wrap around with None
            assert has_expanded_repr(df)
            # Truncate vertically
            assert has_vertically_truncated_repr(df)

    with option_context("display.max_rows", None):
        with option_context("display.max_columns", 0):
            assert has_horizontally_truncated_repr(df)
