# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("mode.sim_interactive", True, "display.max_columns", 20):
    df = DataFrame(
        np.random.randn(5, 3), columns=["a" * 90, "b" * 90, "c" * 90]
    )
    rep_str = repr(df)

    assert len(rep_str.splitlines()) == 20
