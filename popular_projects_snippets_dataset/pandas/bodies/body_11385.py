# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_internals.py
# ensure we can switch the value of the option within one session
# (assuming data is constructed after switching)

# using the option_context to ensure we set back to global option value
# after running the test
with pd.option_context("mode.copy_on_write", False):
    df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})
    subset = df[:]
    subset.iloc[0, 0] = 0
    # df updated with CoW disabled
    assert df.iloc[0, 0] == 0

    pd.options.mode.copy_on_write = True
    df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})
    subset = df[:]
    subset.iloc[0, 0] = 0
    # df not updated with CoW enabled
    assert df.iloc[0, 0] == 1

    pd.options.mode.copy_on_write = False
    df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})
    subset = df[:]
    subset.iloc[0, 0] = 0
    # df updated with CoW disabled
    assert df.iloc[0, 0] == 0
