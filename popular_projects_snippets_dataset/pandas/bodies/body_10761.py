# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# Regression test for (#22487)
df = DataFrame(
    {
        "user": ["A", "A", "A", "A", "A"],
        "connections": [4970, 4749, 4719, 4704, 18446744073699999744],
    }
)
assert df.groupby("user")["connections"].mean()["A"] == 3689348814740003840
