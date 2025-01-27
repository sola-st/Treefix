# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# display.max_dir_items increaes the number of columns that are in __dir__.
columns = ["a" + str(i) for i in range(420)]
values = [range(420), range(420)]
df = DataFrame(values, columns=columns)

# The default value for display.max_dir_items is 100
assert "a99" in dir(df)
assert "a100" not in dir(df)

with option_context("display.max_dir_items", 300):
    df = DataFrame(values, columns=columns)
    assert "a299" in dir(df)
    assert "a300" not in dir(df)

with option_context("display.max_dir_items", None):
    df = DataFrame(values, columns=columns)
    assert "a419" in dir(df)
