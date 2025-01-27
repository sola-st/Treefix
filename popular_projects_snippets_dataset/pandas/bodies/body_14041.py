# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("mode.sim_interactive", True):
    df = DataFrame(np.random.randn(10, 4))
    assert "\\" not in repr(df)
