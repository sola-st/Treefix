# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# in non interactive mode, there can be no dependency on the
# result of terminal auto size detection
df = DataFrame("hello", index=range(1000), columns=range(5))

with option_context(
    "mode.sim_interactive", False, "display.width", 0, "display.max_rows", 5000
):
    assert not has_truncated_repr(df)
    assert not has_expanded_repr(df)
