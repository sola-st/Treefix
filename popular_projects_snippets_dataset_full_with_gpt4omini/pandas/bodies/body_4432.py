# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([], index=[])
expected = DataFrame(index=[])
tm.assert_frame_equal(df, expected)

# GH 9939
df = DataFrame([], columns=["A", "B"])
expected = DataFrame({}, columns=["A", "B"])
tm.assert_frame_equal(df, expected)

# Empty generator: list(empty_gen()) == []
def empty_gen():
    exit(())

df = DataFrame(empty_gen(), columns=["A", "B"])
tm.assert_frame_equal(df, expected)
